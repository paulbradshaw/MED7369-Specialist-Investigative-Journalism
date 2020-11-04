# Looking at company information in the US (notes from Peter Geoghegan)

Many companies will have parents or related companies based in the US. 

## Example: Facebook UK

Take the example of Facebook UK. [On Companies House look under 'Persons with significant control'](https://beta.companieshouse.gov.uk/company/06331310/persons-with-significant-control)

It lists Facebook, Inc., registered in Delaware with the number 3835815.

[Search for that company on OpenCorporates](https://opencorporates.com/companies?jurisdiction_code=&q=Facebook%2C+Inc.&utf8=%E2%9C%93). 

There are many results including "Facebook Inc" (no comma), but you can use the filters on the right to [narrow those down to companies registered in Delaware](https://opencorporates.com/companies/us_de?q=Facebook%2C+Inc.&utf8=%E2%9C%93).

The one we want also has the same registration number, which is part of a structured URL: https://opencorporates.com/companies/us_de/3835815

On this page you will see a link to the **source** of the information: [Delaware Department of State: Division of Corporations](http://www.corp.delaware.gov/). You can click through to this to search for the company's records there. 

Note that in the US companies are registered at the state level, so you have to search within that specific register.

*PS: Notice on the right that someone has [created a corporate grouping for this entity](https://opencorporates.com/corporate_groupings/facebook) that also includes Facebook UK.*

Delaware is a "secrecy jurisdiction" (low disclosure, low tax) so you're unlikely to get much information even if you pay the $20 for extra material. 

More generally, private (i.e. not publicly owned by owners of shares) companies in the US have to publish *less* information than in the UK. 

However, public (i.e. listed so people can buy and sell shares in the company) companies in the US have to publish *more* information than in the UK.

Facebook is a listed company so we can search for its filings: that would take us to https://investor.fb.com where you can find links to [its SEC filings, annual reports and quarterly earnings](https://investor.fb.com/financials/?section=secfilings). 

These contain lots of details on staff, pay, spending, income etc.

## Example: Backstreet Boys and Justin Timberlake

If we were interested in the US band Backstreet Boys we could [search for related companies on OpenCorporates](https://opencorporates.com/companies?q=backstreet+boys&utf8=%E2%9C%93).

These could again be traced to a particular register (Delaware, Florida, even Hong Kong) and researched further. Names of officers can be identified and researched - some will merely be companies who exist to register new companies.

We can search for people as well. Use the search bar at the top to specify **Officers** and [search for Justin Timberlake](https://opencorporates.com/officers?q=justin+timberlake&utf8=%E2%9C%93).

This is quite a distinctive name so most matches - not necessarily all - are likely to be the person we are expecting. For more common names we will have to look for other clues of confirmation (or pick up the phone to check).

He is listed as a director of Big Dipper Motors - would this be the same person? More checks would be needed.

He is also a director of a Foundation - would those details appear on 990 filings? (More below)

## Example 3: digging into a political donor: Richard Cook 

Richard Cook is a political donor. He's [listed as a director](https://beta.companieshouse.gov.uk/officers/6YP-Ed7vjPHMkQNAGO9tc-jfS98/appointments) of DDR Recycling Limited.

That is linked to DDR USA. A search on OpenCorporates takes you to the company DDR International Recycling LLC, and the registry in California. This leads to documents including a filing statement, and the person Gerry Gallagher.

Court records on PACER (signing up involves confirming via post) or Pacermonitor (not free) or Courtlistener (free) shows that the company was involved in a fraud case. Richard Cook is named in the documents.

*UPDATE: In November 2020 a [Guardian story on a collapsed deal for NHS masks appears to use some of these techniques](https://www.theguardian.com/society/2020/nov/03/45m-deal-for-nhs-masks-collapses-amid-claims)*
