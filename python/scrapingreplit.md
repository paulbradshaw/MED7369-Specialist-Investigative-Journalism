# Scraping in Python using repl.it

[Repl.it](https://repl.it/) is an online environment for writing and running code. It supports a wide range of languages, including Python. And most importantly of all, it allows you to install libraries such as `scraperwiki`, which is used for scraping and storing the resulting data.

In this tutorial I explain how to do that.



## The final code

```py
import scraperwiki
import lxml.html
import cssselect
#use pandas to convert to downloadable csv
import pandas as pd

# Store the URL in a variable to make it easier to change
urltoscrape = "https://en.wikipedia.org/wiki/List_of_twin_towns_and_sister_cities_in_England"
#Store the base URL which we often need to add to relative links
baseurl = "https://en.wikipedia.org"
#Scrape the webpage at that URL into a new variable called 'html'
html = scraperwiki.scrape(urltoscrape)
#Print the contents of that new object
print(html)

#Convert that html variable into a new lxml.html object
#(this means it is structured like a tree so we can use lxml.html functions on it)
root = lxml.html.fromstring(html)
# Find something on the page using css selectors
#Specifically anything within a dd tag within a dl tag within a dd tag within a dl tag
#Store the results in a variable we call lis - it'll always be a list
lis = root.cssselect('dl dd dl dd')
#Show how many items are in that new list (how many matches)
print(len(lis))
#create a dictionary to store what we are about to extract
record = {}
#loop through those lis
for li in lis:
  #Print the text within that tag and any child tags
  print(li.text_content())
  #This next line is an alternate troubleshooted version in case there are odd characters that cause an error
  #print(li.text_content().encode('utf-8').strip())
  #Store that in the dictionary, under the key 'address'
  record['address'] = li.text_content()
  record['country'] = li.text_content().split(',')[-1]
  #If we were scraping <a > links and wanted to extract the href attribute, we would use this
  #detaillink = baseurl+li.attrib['href']
  #record['link'] = detaillink
  #Save the whole dictionary as a new row in a table in a sqlite database
  scraperwiki.sqlite.save(['address'],record, table_name='twintowns')

#print the results of querying that table in that database
print(scraperwiki.sql.select("count(*) from twintowns"))
#Store the results of another query
polandtowns = scraperwiki.sql.select("* from twintowns where address LIKE '%Poland%'")
#Print the contents of that variable
print(polandtowns)
#Convert that list of dicts into a pandas dataframe
polandtownsdf = pd.DataFrame(polandtowns)
#Export as a CSV file using the .to_csv function https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
polandtownsdf.to_csv('out.csv')

```
