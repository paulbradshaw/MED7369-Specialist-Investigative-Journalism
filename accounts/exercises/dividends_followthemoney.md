# Dividends: follow the money

A good exercise if you want to learn about company accounts is to reverse-engineer a story based on company accounts. Here's a particularly instructive example:

In June 2023 Private Eye reported: 

> "Surescreen Diagnostics Ltd [who were] given a £500m contract for lateral flow tests [during the Coronavirus pandemic] ... recorded profits for 2020/21 of £67m on a turnover of £151m, giving a 45 percent profit rate that would make other Covid profiteers blush (while having its accounting qualified for ropey record-keeping) ...
>
> "£90m was paid in dividends for the two years to parent company Sunscreen Holdings Ltd, owned by brothers Alastair, Alexandr and David Campbell. But instead of paying the brothers a healthy dividend each and being done with it, the Surescreen group last year underwent a series of corporate contortions to get the money out. First, a new holding company, Surescreen Diagnostics Holdings (2022) Ltd, was created. It then drastically reduced its share capital by around £62m, alongside some other corporate tweaks. The effect of reducing share capital, as opposed to paying a dividend, can be to convert what would be income taxable at higher rates into capital gains taxed at 20 percent."

## Finding the dividends

Let's start by finding those dividends.

Look at [the accounts for Surescreen Diagnostics Ltd](https://find-and-update.company-information.service.gov.uk/company/03235601/filing-history) for the year ending 2022.

**Dividends** are listed in most accounts - this is an amount of money paid to shareholders. 

Normally dividends are detailed in one of the **Notes to the accounts** (or a similar phrase, in this case *Notes to the financial statements*). In the 21/22 accounts for Surescreen Diagnostics Ltd, it's note number 7, on page 13.

That note says that the company paid dividends of £36m in 2022 and £54.4m in 2021. So, a total of £90.4m in two years.

## Finding the shareholders

Now we need to work out where that £90m went. 

Once again, dividends are paid to shareholders. And we can find out who owns most of the shares in a company by using Companies House's ability to see **Persons with significant control**.

To find this, go to [the 'People' tab on the company's page](https://find-and-update.company-information.service.gov.uk/company/03235601/officers) on Companies House. By default you'll be shown the *Officers* list. But next to this tab is a [*'Persons with significant control'* tab](https://find-and-update.company-information.service.gov.uk/company/03235601/persons-with-significant-control). Switch to that.

This lists entities that own a lot of shares, and in this case it says "1 active person with significant control": Surescreen Holdings Limited.

At the bottom it gives detail on the "Nature of control": in this case "Ownership of shares – 75% or more"

So we know that Surescreen Holdings Limited owns at least 75% of the shares. 

Usefully, the page also gives their registration number: 09067025. 

Now, for more information we can look for *that* company's accounts...

## Finding details about the shareholder

Search for Surescreen Holdings Limited on Companies House and you'll find it taking you to the URL https://find-and-update.company-information.service.gov.uk/company/09067025. Notice that the number at the end of that URL is the same as the registration number listed earlier: 09067025. That tells you it's the right company (you can also save time by simply pasting that number on the end of the basic URL).

Find the accounts for 2021/22 and look for any information about Surescreen Diagnostics Ltd. 

A good place to look is, again, in the notes to the accounts, specifically information about **investments** and **subsidiaries** (a company owned by a parent company is a subsidiary of that company).

Note 12: Fixed asset investments on page 21 is where we find the information we need: halfway down the page is the beginning of a list of subsidiaries. The first one is Surescreen Diagnostics Limited and the note says that the company is holding 100% of the shares (the 'class of shares' is also given as 'ordinary').

This means it should get 100% of the dividends, which keeps things nice and simple.

## Following the money out of the company

Now we repeat the process from before, looking for [the **Persons with significant control** for this company](https://find-and-update.company-information.service.gov.uk/company/09067025/persons-with-significant-control).

This time we find *another* holding company: Surescreen Holdings (2022) Limited, registration number 14420253, with "75% or more" shares.

But note that underneath this is listed the previous shareholders: three men with the surname Campbell, each of whom owned "More than 25% but not more than 50%" in shares (so perhaps a third each). So the ownership of shares has changed - and we can see when Companies House was *notified* of this, and when their shareholdings *ceased*: 6 December 2022.

Before this date those three men would have been the shareholders and received the dividends - so the £54.4m dividends for the 2020/21 year were likely to have been distributed to them.

Now, it's going to go to this new shareholder: Surescreen Holdings (2022) Limited.

When we look at [that company's Persons with significant control](https://find-and-update.company-information.service.gov.uk/company/14420253/persons-with-significant-control) we can see the same three people listed as shareholders, with what looks like the same proportions of ownership. 

So why create a new intermediate company if ultimately the dividends are going to go to the same people in the same proportions?

## Reducing share capital

If we look at the new holding company's [filing history](https://find-and-update.company-information.service.gov.uk/company/14420253/filing-history) we might get some clues. 

The first document here is the *Incorporation* which lists the shareholders, how many shares they hold, and what type. This might be changed by later documents.

The second document is **Statement of capital** following an allotment of shares on 6 December 2022: GBP 81,000,000
. That's £81m of capital - money - invested into the company, an amount quite close to the £90m in dividends over the past two years. (If you open the document you can see how that capital is split equally between three types of shares that exist in the company: A Ordinary, B Ordinary, and C Ordinary.)

On May 2023 we have a raft of new documents, including two 'Resolutions' about a "Resolution of reduction in issued share capital", and a new **Statement of capital**. This time it is GBP 18,750,000.

What's happened?

Well, firstly, having invested £81m of capital in the business in December, in May that capital has been reduced to £18.75m.

This is a **capital reduction**, and we can [find out more about this](https://www.investopedia.com/terms/c/capitalreduction.asp):

> "A capital reduction is when a company reduces the amount of its share capital, which can be done by making payments to shareholders out of its capital equal to the amount of money paid by a shareholder to acquire the company's shares or by a share buyback ... Share capital reduction is then expected to be paid to shareholders a few months after the entry of reduction in the commercial register."

So £62.25m is being removed from the company, or £20.75 for each of the three shareholders.

[One article about this practice notes](https://galleyandtindle.co.uk/tax-planning-with-capital-reductions/): 

> "As long as the capital is returned directly to your client and not transferred into a reserve first, the capital reduction cannot be treated as a dividend [and taxed as such]. Providing the capital is reduced on a pound-for-pound basis, there will be no capital gain [tax] triggered for your client as the cash will simply be a return of what your client originally paid in. Even though a capital reduction may simply be a return of originally subscribed capital, HMRC might still object to it in certain circumstances and seek to apply anti-avoidance legislation."

But it goes on to give the example of a holding company being created to avoid tax:

> "The [December 2015 HMRC consultation paper on Company Distributions](https://www.gov.uk/government/consultations/company-distributions) issued prior to the [Finance Act 2016] changes, gave the following example of the type of arrangements involving capital reductions that HMRC was seeking to stamp out using the [transactions in securities (TiS)] legislation. HMRC gives the following example.
> 
> Example. Two companies both set up with £100 of share capital that have a P&L reserve of £250,000. One company pays a dividend to its only shareholder of the full £250,000.
>
> The other company undertakes a share-for-share exchange to insert a holding company, Holdco, with this issuing 250,000 new shares to the shareholder as consideration. Holdco now has £250,000 of share capital (in addition to the £100 it was incorporated with) which it reduces and pays out to the shareholder, thereby gaining an income tax advantage.

*Note: one article on capital reduction [explains how it can also be used to create a profit and justify dividends](https://www.taxinsider.co.uk/capital-reduction-techniques-for-owner-managed-companies-part-ta-1)*

