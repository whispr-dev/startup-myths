# AI Gets You Funded. It Doesn't Get You Paid.

### I checked 47,000 Product Hunt launches against real funding records, and 2,800 indie businesses against their revenue. Investors and customers disagree about AI. Oh, and 98% of "#1 Product of the Day" winners never raise a Series A. Here's what predicts it instead.

*By Claudia G. Petersen*

---

In 2019, about one in sixteen Product Hunt launches had anything to do with AI. By 2025 it was one in two.

You'd expect a stampede like that to dilute the prize. It didn't. AI launches from 2025 have so far raised a Series A at more than three times the rate of everything else, and that gap has widened every year since 2022. Investors aren't tiring of AI. They're ordering another round.

So I went looking for the customers.

On Indie Hackers, where founders report what their products actually earn, the picture flips. AI products are *less* likely to reach even $1,000 a month than the boring stuff: invoicing tools, email software, online shops.

Same technology. Same few years. Two scoreboards pointing in opposite directions.

I went through six datasets to find out why. While I was in there, I also found out that the trophy everyone on Product Hunt is chasing predicts almost nothing, and that the thing which *does* predict funding is so unglamorous nobody puts it in a launch-day thread.

Let's take it in order, darlings.

## First, the ground rules

A **Series A** is the first serious round of venture capital, the point where professional investors hand over millions (the median in this data is $15 million) because they think the company is real. It isn't the only kind of success. It is, however, a matter of public record, which makes it rather harder to exaggerate than one's monthly revenue.

My main source is **PHBench**, an academic dataset built by Yagiz Ihlamur, Ben Griffin and Rick Chen. They took every launch that Product Hunt featured on its front page from 2019 to 2025 and matched each one against Crunchbase funding records. The public portion is 47,071 launches. Of those, 372 raised a Series A within 18 months.

That's 0.79%. Hold on to that number. It is the baseline, and everything below is measured against it.

For revenue, I used a scrape of 2,827 products from the Indie Hackers directory, plus smaller Product Hunt and Gumroad datasets as cross-checks. All of it, along with the code, is linked at the end.

## The room got eight times more crowded. The odds didn't drop.

![Chart: share of Product Hunt launches tagged AI, 2019–2025, against Series A rates for AI and non-AI launches](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/article/charts/01_ai_flood_vs_funding.png?raw=true)

The grey bars are the flood: AI's share of all featured launches, from 6% in 2019 to 51% in 2025. The two lines are the odds of raising a Series A.

Both lines fall off a cliff in 2022, and that's not an AI story. That's the year venture capital in general sobered up after the 2021 party. What matters is the *gap between* the lines. In 2022, an AI launch was about one and a half times as likely to get funded as anything else. By 2024, two and a half times. For 2025 launches so far, more than three and a half.

(A caveat on 2025: those companies haven't had their full 18 months yet, so both lines will drift upward. It applies to both equally, so the comparison holds.)

Could it just be that AI launches are flashier and pull more votes? I checked. Using a statistical model that holds votes, team size, market segment and launch year constant, comparing like with like, an AI tag still carries about 1.6 times the odds of a Series A.

So yes. Put "AI" on it, and investors are measurably more interested. No great shock. Here's the other scoreboard.

## Meanwhile, at the till

![Chart: AI versus everything else on two measures, Series A rate and share reaching $1,000 a month](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/article/charts/02_ai_funded_vs_paid.png?raw=true)

On Indie Hackers, 40% of non-AI products in my sample report reaching $1,000 a month. For AI products, it's 31%. Run the same kind of like-for-like model and AI products have roughly 0.6 times the odds of clearing that bar.

Now, I promised you sharp, not convenient, so here is the part a less scrupulous writer would leave in the drawer.

About 90% of Indie Hackers revenue figures are self-reported, and self-reported revenue is a genre of fiction. In this dataset, 86% of self-reported figures above $1,000 are perfectly round thousands. Among figures verified directly through Stripe, the payment processor, it's 3%. People are not earning in round numbers. People are *remembering* in round numbers, generously.

So I re-ran the AI comparison using only the Stripe-verified products. There the gap closes: 38% of AI products reach $1,000 a month against 39% of the rest. It's a small group (just 50 verified AI products), so treat it gently. But the honest summary is this:

**AI gives you a clear edge with investors. With customers, it gives you, at the very best, no edge at all.**

Which is still remarkable. The most hyped technology of the decade, a funding edge that investors widen every year, and at the till it performs exactly like a scheduling app.

One more piece of perspective, because the chart demands it:

![Chart: Series A rate by Product Hunt topic, with AI highlighted mid-table](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/article/charts/05_topics_vs_series_a.png?raw=true)

AI beats the average. It does not beat *plumbing*. APIs, payments, fintech and sales software all convert to Series A at well over twice AI's rate. The things investors fund most reliably are the things you would never bring up at a dinner party. And on Indie Hackers, payments and sales tools sit in the top four for revenue, too. Boring, it turns out, is the one category that wins on both scoreboards.

## About that trophy

Product Hunt crowns a "#1 Product of the Day." Founders plan for months around it. There are consultants. There are Slack groups. There are people who will sell you a launch-day checklist.

![Chart: Series A rate by daily rank on launch day](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/article/charts/03_daily_rank_vs_series_a.png?raw=true)

There are 1,782 daily winners in the data. Thirty-nine of them raised a Series A within 18 months. That's 2.19%, which means **97.8% did not.**

To be fair to the trophy: 2.19% is nearly three times the baseline, and the chart does slope the right way. Rank isn't *meaningless*. It's just weak. Here's a cleaner way to see how weak: pick one funded launch and one unfunded launch at random, and ask which had more votes. If votes predicted perfectly, the funded one would win every time. If votes were noise, half the time. The real answer is 68%. Better than a coin. Not by a margin you'd bet a company on.

Winning Product Hunt is a champagne mimosa at breakfast. It's lovely, it photographs beautifully, and it tells you almost nothing about how the rest of the day is going to go.

## Here's what does

![Chart: Series A rate by number of makers listed on the launch](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/article/charts/04_makers_vs_series_a.png?raw=true)

Every Product Hunt launch lists its "makers," the people who built it. Count them, and you get the single strongest signal in the entire dataset.

One maker: a Series A rate of 0.25%. **One in 403.** Two makers: one in 98. Three: one in 74. Six or more: **one in 35.** It climbs at every step, and it survives the like-for-like model too: holding votes, topic and year constant, a launch with three or more makers has about 4.7 times the odds of a solo one. The Indie Hackers data agrees: 56% of multi-founder products report reaching $1,000 a month, against 29% of solo ones, and that gap holds among the Stripe-verified.

Before anyone goes co-founder shopping, read this next paragraph twice.

Of the companies that raised a Series A, 88% **already had seed funding** when they launched. A launch with six makers is, very often, not six friends in a garage. It's a company that already has money, an office and a payroll, turning up on Product Hunt as a marketing exercise. Headcount isn't necessarily *causing* the funding. To a large degree it's *measuring* something that already happened.

Think of it as a wedding. The guest list doesn't create the marriage, but its length tells you a good deal about who was already invested.

So the claim I'll stand behind is the narrow one: **solo launches almost never turn into venture-backed companies.** Whether that's because solo founders can't, or because most of them, quite sensibly, don't want to, this data can't say. Plenty of one-person businesses are after a good living, not a board of directors.

## And the money, when it comes, goes to almost no one

![Chart: Lorenz curves for Indie Hackers revenue, Gumroad sales and Product Hunt votes](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/article/charts/06_lorenz_money_vs_applause.png?raw=true)

This chart lines products up from poorest to richest and asks what share of the total they hold. Perfect equality would be the dotted diagonal. The further a curve sags below it, the more the winners take. The sag gets summarised in one number, the **Gini coefficient**: 0 means everyone has the same, 1 means one person has everything. The most unequal countries on Earth score around 0.6.

Indie Hackers revenue scores **0.92**. The top 1% of products, 28 of them, take 52% of all the revenue. I checked a completely unrelated platform, Gumroad, to see if that was a fluke. It came back at **0.91**. Two different marketplaces, two different kinds of product, and the curves sit almost on top of each other.

Now look at the blue line: votes among featured Product Hunt launches. Gini 0.37. Practically Scandinavian.

That's the finding in one picture. **Applause is shared out. Money is not.** Once you're on the front page, nearly everyone gets a respectable crowd, which is precisely why the crowd tells you so little.

## What I'd actually take from this

If you're building something on your own, the useful reading isn't "give up." It's "stop taking applause for evidence."

- **Upvotes are not customers.** They're distributed generously and they predict weakly.
- **An AI label is a fundraising asset.** On this evidence it is not a revenue asset. If you aren't fundraising, it's decoration.
- **The dull categories win twice.** Payments and sales tooling top the tables for funding *and* revenue. Nobody's doomscroll was ever stopped by an invoicing API, and that is rather the point.
- **Going solo is a fine way to build a business and a poor way to raise venture capital.** Know which one you're doing.

And if someone tries to sell you a launch-day playbook, ask them, sweetly, what happened to the other 97.8%.

## The small print, because I'd rather you heard it from me

- Every dataset here is a volunteer sample: people who chose to launch on Product Hunt, list on Indie Hackers or disclose Gumroad sales. None is a census of all startups. Read every claim as "among products on this platform."
- The Indie Hackers scrape over-represents higher earners (it appears to include the whole $10k-and-up leaderboard plus a scatter of the rest), so I've compared groups *within* it and avoided quoting it as a real-world success rate.
- Funding matches rely on Crunchbase, which is patchier outside the US. Some funded companies will have been counted as unfunded.
- These are associations, not recipes. Nothing here shows that changing one thing about your launch would change your outcome.

## Data, code and charts

Everything is reproducible. Clone it, run it, tell me where I'm wrong.

- **Full repository:** [github.com/YOUR-USERNAME/YOUR-REPO](https://github.com/YOUR-USERNAME/YOUR-REPO)
- **Analysis script:** [combined_analysis.py](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/combined_analysis.py)
- **Chart script:** [article/make_charts.py](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/article/make_charts.py)
- **Full findings sheet:** [FINDINGS.md](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/FINDINGS.md)
- **Table, inequality by dataset:** [lottery_table.csv](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/lottery_table.csv)
- **Table, Series A rate by topic:** [phbench_topic_rates.csv](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/phbench_topic_rates.csv)
- **Table, Indie Hackers revenue by category:** [ih_category_table.csv](https://github.com/YOUR-USERNAME/YOUR-REPO/blob/main/ih_category_table.csv)

**Sources.** PHBench: Ihlamur, Griffin & Chen (2026), *PHBench: A Benchmark for Predicting Startup Series A Funding from Product Hunt Launch Signals*, arXiv:2605.02974, licensed CC BY 4.0; access is requested via [huggingface.co/datasets/ihlamury/phbench](https://huggingface.co/datasets/ihlamury/phbench), so the raw file is not redistributed in my repository. Indie Hackers product directory scrape (2,868 products). Gumroad market data (CC BY 4.0). Product Hunt launch archives via Kaggle.

---

*Claudia G. Petersen writes about the numbers underneath the things people say with great confidence.*
