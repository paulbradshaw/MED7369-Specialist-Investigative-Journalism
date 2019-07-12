# Benford's Law - notes from CIJ Summer School 2019

*[See document here](https://docs.google.com/document/d/17KdK2xadn_w8bOO2B4ILh0D8pVj7axt6bt2Koi7Svvw/edit?usp=sharing) for more details.*

You need to be working with data that covers a wide enough range of amounts, e.g. from 100-10,000. There shouldn't be any hard maximums or minimums.

Start with the [example spending data](https://docs.google.com/spreadsheets/d/1q32GEcsfTUOYJ01Qbn0peoMCdTIoDhOoa6Wp9z7fsGA/edit?usp=sharing).

Copy down the formulae in cells F2-H2 so that they extract the first and second digits for the amounts.

Sheet 2 ('calc_debtcancel'): A man is cancelling debts on credit cards.

> "What's caught him out is that he has a systemic approach to what he does.

> "He doesn't have any control over it. He's handing the credit cards to family and friends and cannot control what they do with it."

`=LOG10(1+(1/C2))`

When we subtract with the difference we end up with this arc. The blue line is what Benford's Law should show, the red is what the data shows.

An extreme Z score indicates the data is unlikely to occur given the distribution.

If I increase the number of records in B1 you will see that the Z scores will jump.

Sheet 3 ('bigcorp') shows the declared results of a large corporation who we think might be rounding up.

Copy the formulae in F-G down

## The histogram

Sheet 4 ('calc_bigcorp') takes the analysis forward. Look for the drop off at 99 where it's being rounded up instead of actual numbers

Next sheet ('seconddigit_bigcorp') shows an analysis of second digits which demonstrates this further (EP = expected proportion, AP = actual proportion)

Sheet 6 ('embezzle') is about embezzlement. Copy F-G down.

Large spike at 50.

Follow through to sheet 'calc_embezzle' and copy formulae down to see spike.

It isn't a close fit to Benford's Law but we can compare it to **Nigrini’s Second last theorem**.

In the next sheet 'summation_embezzle'

This is looking at the value amount when added together. A large spike would be one-off occurrences, but if you see significant purchases that are regular and have the same two digit starting combination

We see spikes along the course rather than just at the start.

These are examples of double-billing.

> "She started billing for people having heart operations who didn't need them."

Looking for:

* Unusual distribution of values
* Large values of the same sum
* People rounding for psychological effect, hit targets for bonuses etc.

Example: imports into Turkey before and after tax rate went up (evidence of smuggling)

Not all datasets are suitable for Benford's Law. You want to be sure that the mean is higher than the median. Lots of small values.

Testing against previous years' data helps improve your test.
