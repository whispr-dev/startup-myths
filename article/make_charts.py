"""Standalone, publication-sized charts for the article.
Run from the project root:  python article/make_charts.py data
Writes article/charts/01..06_*.png
"""
import ast, os, sys
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1] if len(sys.argv) > 1 else "data"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts"); os.makedirs(OUT, exist_ok=True)
INK, AI_C, REST_C, GREY = "#1a1a1a", "#c1121f", "#2a6f97", "#b8b8b8"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": INK, "axes.titleweight": "bold", "axes.titlesize": 15, "axes.titlelocation": "left"})
def save(fig, name, src):
    fig.text(0.01, 0.005, src, fontsize=8, color="#666"); fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(OUT, name), dpi=160, facecolor="white"); plt.close(fig); print("wrote", name)

pb = pd.read_csv(os.path.join(D, "phbench_public_train.csv"), low_memory=False); pb["y"] = pb.label_series_a_within_18m.astype(int)
base = 100*pb.y.mean(); SRC = "Data: PHBench public training split (Ihlamur, Griffin & Chen, 2026), 47,071 featured Product Hunt launches. Analysis: author."

# 01 — AI flood vs funding rate
g = pb.groupby("launch_year"); share = 100*g.is_ai_topic.mean()
ai = 100*pb[pb.is_ai_topic == 1].groupby("launch_year").y.mean(); non = 100*pb[pb.is_ai_topic == 0].groupby("launch_year").y.mean()
fig, ax = plt.subplots(figsize=(10, 5.6)); ax2 = ax.twinx(); ax2.bar(share.index, share, color=GREY, alpha=.35, width=.7); ax2.set_ylim(0, 100)
ax2.set_ylabel("% of launches tagged AI (grey bars)", color="#777"); ax2.spines["right"].set_visible(True); ax2.spines["right"].set_color("#ccc")
ax.plot(ai.index, ai, "o-", color=AI_C, lw=2.5, label="AI-tagged launches"); ax.plot(non.index, non, "s-", color=REST_C, lw=2.5, label="Everything else")
ax.set_zorder(ax2.get_zorder()+1); ax.patch.set_visible(False); ax.set_ylabel("% raising a Series A within 18 months"); ax.set_ylim(0, 2.2); ax.legend(frameon=False, loc="upper right")
ax.set_title("The room got eight times more crowded. The odds didn't drop.")
save(fig, "01_ai_flood_vs_funding.png", SRC + " 2025 cohort not yet fully resolved.")

# 02 — AI: funded vs paid (two scoreboards)
ih = pd.read_csv(os.path.join(D, "full_data.csv")); ih = ih[ih.revenue.astype(str).str.startswith("$")].copy()
ih["rev"] = ih.revenue.str.replace(r"[$,]", "", regex=True).astype(float).clip(lower=0)
def tl(s):
    try: return ast.literal_eval(s)
    except Exception: return None
ih["tagl"] = ih.tags.map(tl); ih = ih[ih.tagl.notna()]; ih["AI"] = ih.tagl.map(lambda L: "AI" in L)
f_ai, f_non = 100*pb.y[pb.is_ai_topic == 1].mean(), 100*pb.y[pb.is_ai_topic == 0].mean()
p_ai, p_non = 100*(ih.rev[ih.AI] >= 1000).mean(), 100*(ih.rev[~ih.AI] >= 1000).mean()
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 5.2))
for axx, vals, ttl, fmt in ((a, (f_ai, f_non), "FUNDED\nraised a Series A within 18 months", "{:.2f}%"), (b, (p_ai, p_non), "PAID\nreached $1,000 a month in revenue", "{:.0f}%")):
    bars = axx.bar(["AI", "Everything else"], vals, color=[AI_C, REST_C], width=.6); axx.set_title(ttl, fontsize=12); axx.set_yticks([])
    axx.spines["left"].set_visible(False)
    for r, v in zip(bars, vals): axx.text(r.get_x()+r.get_width()/2, v, fmt.format(v), ha="center", va="bottom", fontsize=15, fontweight="bold")
    axx.set_ylim(0, max(vals)*1.25)
fig.suptitle("Same technology, two scoreboards", x=0.01, ha="left", fontsize=15, fontweight="bold")
save(fig, "02_ai_funded_vs_paid.png", f"Left: PHBench, n={len(pb):,}. Right: Indie Hackers product directory, n={len(ih):,} (mostly self-reported revenue). Analysis: author.")

# 03 — what #1 of the day is worth
rk = pb[pb.has_daily_rank == 1]; grp = [("#1", rk.daily_rank == 1), ("#2–3", rk.daily_rank.between(2, 3)), ("#4–5", rk.daily_rank.between(4, 5)), ("#6–10", rk.daily_rank.between(6, 10)), ("#11+", rk.daily_rank >= 11)]
vals = [100*rk.y[m].mean() for _, m in grp]; ns = [int(m.sum()) for _, m in grp]
fig, ax = plt.subplots(figsize=(10, 5.2)); bars = ax.bar([f"{l}\n(n={n:,})" for (l, _), n in zip(grp, ns)], vals, color=[AI_C]+[REST_C]*4, width=.65)
for r, v in zip(bars, vals): ax.text(r.get_x()+r.get_width()/2, v, f"{v:.2f}%", ha="center", va="bottom", fontweight="bold")
ax.axhline(base, color=INK, ls="--", lw=1); ax.text(4.45, base+.04, f"all launches {base:.2f}%", ha="right", fontsize=10)
ax.set_ylabel("% raising a Series A within 18 months"); ax.set_xlabel("Daily rank on launch day"); ax.set_ylim(0, max(vals)*1.25)
ax.set_title(f"The trophy: {100-vals[0]:.0f}% of daily winners never raised a Series A")
save(fig, "03_daily_rank_vs_series_a.png", SRC); n1, r1 = ns[0], vals[0]

# 04 — makers
pb["mk"] = pd.cut(pb.maker_count, [0, 1, 2, 3, 5, 99], labels=["1", "2", "3", "4–5", "6+"]); t = 100*pb.groupby("mk", observed=True).y.mean(); tn = pb.groupby("mk", observed=True).y.size()
fig, ax = plt.subplots(figsize=(10, 5.2)); bars = ax.bar([f"{i}\n(n={tn[i]:,})" for i in t.index], t.values, color=[AI_C]+[REST_C]*4, width=.65)
for r, v in zip(bars, t.values): ax.text(r.get_x()+r.get_width()/2, v, f"{v:.2f}%\n1 in {round(100/v):,}", ha="center", va="bottom", fontweight="bold", fontsize=11)
ax.axhline(base, color=INK, ls="--", lw=1); ax.set_ylim(0, t.max()*1.3); ax.set_ylabel("% raising a Series A within 18 months"); ax.set_xlabel("People listed as makers on the launch")
ax.set_title("Headcount on launch day vs. Series A odds")
save(fig, "04_makers_vs_series_a.png", SRC + " Launches with no makers listed omitted.")

# 05 — topics
tc = [c for c in pb.columns if c.startswith("topic_") and c != "topic_count"]
tr = pd.Series({c[6:].replace("_", " ").title().replace("Api", "API").replace("Saas", "SaaS").replace("Ios", "iOS"): 100*pb.y[pb[c] == 1].mean() for c in tc}).sort_values()
fig, ax = plt.subplots(figsize=(10, 7)); ax.barh(tr.index, tr.values, color=[AI_C if i == "Artificial Intelligence" else REST_C for i in tr.index])
for i, v in enumerate(tr.values): ax.text(v+.03, i, f"{v:.2f}%", va="center", fontsize=10)
ax.axvline(base, color=INK, ls="--", lw=1); ax.set_xlabel("% raising a Series A within 18 months"); ax.set_title("Plumbing beats glamour: Series A rate by topic")
save(fig, "05_topics_vs_series_a.png", SRC + " A launch can carry several topics.")

# 06 — Lorenz: money vs applause
gs = pd.read_csv(os.path.join(D, "gumroad-sales.csv")); gs = gs[pd.to_numeric(gs.sales_count, errors="coerce").notna()]
gross = pd.to_numeric(gs.sales_count)*pd.to_numeric(gs.price_usd, errors="coerce").fillna(0)
def gini(x):
    x = np.sort(np.asarray(x, float)); n = len(x); return (2*np.sum(np.arange(1, n+1)*x)/(n*x.sum())) - (n+1)/n
fig, ax = plt.subplots(figsize=(10, 6))
for lab, v, c, ls in (("Indie Hackers revenue", ih.rev, AI_C, "-"), ("Gumroad gross sales", gross, "#e07a00", "-"), ("Product Hunt votes (featured launches)", pb.votesCount, REST_C, "-")):
    xs = np.sort(np.asarray(v, float)); ax.plot(np.linspace(0, 100, len(xs)), 100*np.cumsum(xs)/xs.sum(), color=c, lw=2.5, ls=ls, label=f"{lab} — Gini {gini(v):.2f}")
ax.plot([0, 100], [0, 100], "k--", lw=.8, label="Perfect equality"); ax.legend(frameon=False, loc="upper left")
ax.set_xlabel("Products, poorest to richest (%)"); ax.set_ylabel("Share of all revenue / votes they hold (%)"); ax.set_title("Applause is shared out. Money is not.")
save(fig, "06_lorenz_money_vs_applause.png", "Data: Indie Hackers directory scrape (n=2,827), Gumroad sales disclosers (n=316), PHBench (n=47,071). Analysis: author.")

print(f"\nFACTS  #1 winners n={n1}, raised={int(round(n1*r1/100))}, rate={r1:.2f}%  | AI funded {f_ai:.2f} vs {f_non:.2f} | AI paid {p_ai:.1f} vs {p_non:.1f}")
print("AI share by year:", share.round(1).to_dict()); print("AI rate:", ai.round(2).to_dict()); print("non-AI rate:", non.round(2).to_dict())
s = ih[ih.revenue_explanation.eq("stripe-verified revenue")]; print(f"Stripe-only AI check: AI n={s.AI.sum()} ge1k={100*(s.rev[s.AI]>=1000).mean():.1f}% vs non-AI n={(~s.AI).sum()} {100*(s.rev[~s.AI]>=1000).mean():.1f}%")
