# Notes on scraping law

In [this video a panel discusses the range of legal issues that scraping raises](https://www.bigmarker.com/oxylabs/web-scraping-legal-perspective?bmid=1b64733cb114). Here are some key notes:

Sanaea Daruwalla from 15 mins, notes that you need to consider:

* What you're scraping
* How you're scraping
* What you're doing with that

The top 3 things are:

* Copyright issues
* Contract laws and how they relate to T&Cs, factors such as [Browsewrap Versus Clickwrap](https://www.termsfeed.com/blog/difference-browsewrap-clickwrap), whether it's public or non-public data
* Personal data: make sure you know what personal data is, and what laws you might run into (GDPR, CDPA)

The Computer Fraud and Abuse Act in the US - supposed to be an anti-hacking law, is another.

Allen O’Neil at 22 mins:

Database Copyright Law says that if we have a database then we have copyright in it. But if it's just a listing of something that happens then copyright doesn't apply. On the other hand if I add value to it then I can. The question is to what extent you can argue that you've added value, in a similar way to how patent law operates and differs in application between the EU and US.

Mindaugas Civilka (36 mins): 

* copyright and intellectual property law
* privacy law
* information security law - these are dormant in most European countries. In Lithuania there are clauses in criminal laws that make it illegal to access information system even for private use
* contractual law which is the weakest defence you can have as a system owner
* competition law 

Depends on how the owner of the asset behaves, what message they send. What if they want to reserve part of the information for themselves. 

We have cases where it depends on whether the scraper declares itself - "these are the crawlers" or "these are the robots" or whether it disguises that. Being a robot is not a problem as long as you declare it, but concealing it might be a problem. 

Then it depends whether the domain is public or private data, structured or unstructured. Unstructured is less protected.

The second approach that courts take is the "shopping mall" approach - "What's legal offline should be legal online". So if there was a landlord and you are a tenant, what rules do you abide by when entering the shopping mall. "No photos" is at the heart of it. Writing the prices down is not a problem, but taking a photo is. But why? What public good or private good is being defended? That concept is difficult to apply because it has so many angles.

Competition law is important. It can be designed to protect the secondary markets from the dominant upstream market. In other words if the online platform is big enough it cannot foreclose access to the public domain for smaller competitors who would create products in the secondary market. Skyscanner is an example of [a competitor in] the secondary market, as is Expedia. 

Also, of course, the [Robots.txt](https://developers.google.com/search/docs/advanced/robots/intro) file

## Good practice

Sanaea Daruwalla (44 mins):

Having a good practice guide is useful - it helps explain to those who don't understand scraping. It also means people don't have to understand the law - just understand the triggers that should "bring you to the legal department and then we will review the project".

[Zyte's scraping best practices are available here](https://www.zyte.com/learn/web-scraping-best-practices/)

The Financial and Information Services Association (FISD) has an [Alternative Data Council](https://history.siia.net/Divisions/FISD-Financial-Information-Services-Association/Programs/Alternative-Data-Council) which is also putting together some best practice specific to the financial sector.

## Receiving a cease and desist letter

Bradley Gross (47 mins): need to consider whether you feel the scope of the law has changed to justify the letter. In the light of the HiQ and other cases - do you "wait and see" what decisions are reached? Do you create a checklist/guidelines?

Steven Callahan (50 mins): there is no one size fits all but consider:

* Who is issuing the letter? What is the likelihood that they will actually do anything? 
* What is the site you are scraping?

You can ignore it and "9 times out of 10 if you ignore it nothing will come of it"

You can also respond and explain why you disagree. "You are unlikely to change their mind but later on you will be able to show that you responded in good faith"

You can sue them. In the US you can file a declaratory judgement lawsuit "where the accused strikes first and brings a lawsuit saying no I am not liable". This can be a good strategy depending who is sending the letter. For a big company like Google it's not a good idea, but a smaller company may not have the resources to defend.

You can decide it's not important enough and let it go.

## What is public?

The shopping mall analogy is useful again here. Are there signals that the contents may not be public for all? Is there a security guy at the door?

A checklist is also useful: is the data open and available? Do you have to sign in? It could be open for a faulty reason, including still-open access that has since changed, or have personal or sensitive information. 

Ryanair won out on the fact that the scraper signed in, and accepted the T&C as a robot.

You need to keep up to date not only with the law but with your own governance - update best practice and guidelines to reflect that.

If you have to explicitly agree/consent to T&C then it's important to read those.

What about when it blocks IP addresses or uses Captcha? Have they created a de facto clickthrough agreement by doing that? 

Bradley Gross (63 mins): "I don't think that the case law would support a de facto clickthrough agreement just because they have made it more difficult. There's no conditions no credentialised gateway. All they've said is that you can't make a right turn [to get to the information]"

It's better is the data is not unique and **copyrightable**. 

Allen O’Neil (65 mins): Dublin Law Society discussion said it is reasonable to expect when making a public website that someone go in and take a reasonable amount of data points. But using a scraper to take [more] was not "reasonable" - it's about the value created. It wasn't for a **competing** company to come in and take the entire system as one lump. 

Mindaugas Civilka (68 mins): "We are defending the look and feel of the shop, it's meant for the public's use. It's another thing when a competitor starts to copy the whole essence of what the shop consists of.

"Public data is a concept which is well known in European law and we have a specific [2019 regulation](https://ec.europa.eu/digital-single-market/en/european-legislation-reuse-public-sector-information) [on that] which [defines it as that which] has a specific value for society [such as] geospatial data, company data."

[More from the European legislation on open data and the re-use of public sector information](https://ec.europa.eu/digital-single-market/en/european-legislation-reuse-public-sector-information) on the categories:

> The thematic categories of high-value datasets, as referred to in Article 13(1) of the Directive, are:
1. Geospatial
2. Earth observation and environment
3. Meteorological
4. Statistics
5. Companies and company ownership
6. Mobility

## Notes

[Browsewrap Versus Clickwrap](https://www.termsfeed.com/blog/difference-browsewrap-clickwrap):

> "A browsewrap agreement is when you place links to your legal agreements somewhere on your website (usually at the bottom) ... A clickwrap agreement, on the other hand, is when you require users to actively give consent, such as by checking a box to confirm that they have read and agree to the terms of your agreements, or clicking an "Accept" button next to a statement that informs the user that by clicking, they are accepting the terms.



