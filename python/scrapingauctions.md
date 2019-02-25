# Python: scraping an auctions site

Here's the scenario: the Bureau Local are coordinating an investigation into councils selling public land in order to plug gaps in services caused by cuts, and to fund redundancies. You have noticed that one company in particular - SDL Auctions - seems to be coordinating a large majority of auctions of property owned by councils.

In order to establish the scale of these sales, you need to collect information on all the auctions held by this company. Luckily, [there is a page on their site which lists every single auction, and each property in those, since 2009](https://www.sdlauctions.co.uk/property-list/).

You need to scrape all those auctions so that you can answer questions such as: has the volume of auctions handled by this company increased, and by how much? How many of the auctions mention words like 'council's fees' or 'former care home'?

This tutorial outlines how to adapt the template code on scraping site Morph.io to scrape that page.

## Start with the template code

Sign up for an account on GitHub, if you haven't already, and then log in to Morph.io with your GitHub account.

Click 'New Scraper' and choose Python as the language. Give it a name (without spaces) - you don't need to describe the data it is collecting.

After a few moments it will create a new page on Morph.io where you can run your new scraper. The *code*, however, is hosted elsewhere, in your GitHub account.

Look for the link to that code on the right of the page - it should say *scraper.py*. Right-click on that link and open it in a second tab, so that you have two tabs open:

* One tab with your Morph.io page to *run* the scraper;
* One tab with your Python code hosted on GitHub, where you can *edit* the scraper.

The code created by Morph.io should look like this:

```py
# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
```

### Comments and commenting out

All of the code is *commented out*: that means that each line starts with a hash symbol, `#`, which turns it into a comment rather than working code.

So at the moment, if you ran this code nothing would happen.

The idea is that you can *uncomment* some of these lines of code in order to use it.

The first two lines tell you just that:

```py
# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
```

You should leave these as comments, because that's what they are (you can tell because they are just normal sentences).

The next two lines, however, are lines of code that have been commented out:

```py
# import scraperwiki
# import lxml.html
```

Uncomment these by removing the hash and the space so that it looks like so:

```py
import scraperwiki
import lxml.html
```

You will notice that the code now turns from grey (inactive) to different colours. The colouring helps to indicate the type of code. For example, *commands*, *variables*, *numbers*, *strings*, and so on. We'll touch on each of these as we go.


### Importing libraries

Both of the lines you have just uncommented import a **library**.

The word `import` is a command that you use to bring a library into your code, and it is followed by the name of the library.

Libraries are collections of *functions* and other code that has been written by other people to solve a particular collection of problems.

The `scraperwiki` library was written to solve scraping-related problems such as grabbing a webpage from a URL, and storing data.

The `lxml.html` library was written to solve HTML-parsing problems such as drilling down into a particular part of a webpage (which we need to grab data in that part).

You can find out more by googling for the name of the library, 'python' and 'documentation', e.g. "lxml.html python documentation".

## Scraping the whole webpage

Now uncomment the next line of code - note that the comment above it explains what the code does:

```py
# Read in a page
html = scraperwiki.scrape("http://foo.com")
```

This line of code goes to a specified URL, scrapes all the HTML from that page (using a function from the `scraperwiki` library called `scrape()`), and puts it in a new variable we call `html`.

For the purposes of using this code, all you really need to know is that you can *change the URL to scrape a different weppage*.

We are scraping this URL: `https://www.sdlauctions.co.uk/property-list/`

So the code needs to be changed to this:

```py
# Read in a page
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
```

Note that the URL is in quotation marks: it is being supplied as a *string*.

Now we have stored the whole webpage we can test that it has worked by adding a `print()` command to see that variable `html`. It's a good idea to add a comment as well to explain to yourself what the new line of code is doing:

```py
# Read in a page
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
# Print the variable html containing the webpage
print(html)
```

You can run this code to test that it works.

## Drilling down into the page

Now we have to full page, we want to drill down to a specific *part* (or parts) of that.

Uncomment the next 2 lines of code:

```py
# Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("div[align='left']")
```

Again, there's a comment to explain what's happening: these lines dig further into the webpage using "css selectors" (the first line converts it to a type of variable it can do this with, but you don't need to worry about that, or change it).

Specifically, the CSS selector being used is: `"div[align='left']"` - this is the only bit you need to change when adapting this code for different pages.

 You might want to add your own more specific comments to help with this, like so:

 ```py
 # Find something on the page using css selectors
 root = lxml.html.fromstring(html)
 #Change "div[align='left']" to a different CSS selector to grab something else
 root.cssselect("div[align='left']")
 ```

At the moment this code will look for anything inside a HTML tag `<div align="left">`. To adapt this for your own purposes, you first need to identify the HTML code that you want to target in your webpage.

It's worth googling 'CSS selectors' to find out a bit more about them, and keep referring to guidance on CSS selectors as you try to come up with your own.

## Changing the selectors so they work for your page

Make sure you are looking at that webpage https://www.sdlauctions.co.uk/property-list/ in the browser Chrome or Firefox (this won't work in Safari or Internet Explorer/Edge).

Find an example of the piece of information you want to scrape: one of the auction listings (for example "Former Hillcrest HOP, Kenilworth Drive") then *right-click* on that text and select *Inspect* or *Inspect element*.

A window should appear on the screen showing the HTML code surrounding that element. It will look something like this:

```html
<li>
  <p>
    <a href="/property/20993/residential-development-for-auction-ilkeston/" title="Former Hillcrest HOP, Kenilworth Drive, Kirk Hallam, Ilkeston, Derbyshire DE7 4FJ">
      Former Hillcrest HOP, Kenilworth Drive, Kirk Hallam, Ilkeston, Derbyshire DE7 4FJ
    </a>
  </p>
</li>
```

If you look at the HTML tags around this information (tags are coloured purple) you should see a few options:

* You can target the `<a ...>` tags that the text is in
* You can target the `<p>` tags
* You can target the `<li>` tags
* You could target a combination of those tags
* You could target the `<a ...>` tags with a particular `title=` attribute (attributes are coloured orange, and the values blue)

**Trial and error** is a very important method in identifying the best approach, but you can also make a guess as to which approach might be most effective. For example:

* The `<a ...>` tag is used for all links, so you will capture other links if you use this alone
* Likewise `<p>` tags are used for any paragraph, so you'll get other information you don't want
* The `<li>` tag is for a list item, so that might be more specific if there aren't any other lists on this page
* The `title =` attribute is too specific: `title="Former Hillcrest HOP, Kenilworth Drive, Kirk Hallam, Ilkeston, Derbyshire DE7 4FJ"` is unique to just this one item, so it won't capture other ones.

So, some sort of *combination* of tags is likely to be more effective than those other options.

To create a CSS selector for 'an `a` tag within a `p` within an `li`' you simply list those tags in the order you want to look, as if going into one and then the other, like so:

`li p a`

What this means is: find all the `li` tags on this page, then in each of those look for any `p` tags, then within each of those, look for any `a` tags. It will only bring back results where it can follow the full path.

Change the selector in your code to look for `li p a` - and add a comment too:

```py
# Find something on the page using css selectors
root = lxml.html.fromstring(html)
#Change "li p a" to a different CSS selector to grab something else
#Look for an a tag inside a p tag inside an li tag
root.cssselect("li p a")
```

Save the changes to your code, and run it to check that it works.

## Saving the results

The code might run fine, but you can't actually see what it has grabbed.

That line `root.cssselect("li p a")` doesn't actually store the matching information or print it, or do anything.

Change that line so that the results are stored in a new variable, and then add an extra line to print it. Add some comments too:

```py
# Find something on the page using css selectors
root = lxml.html.fromstring(html)
#Change "li p a" to a different CSS selector to grab something else
#Look for an a tag inside a p tag inside an li tag
#Store the matches in 'matchedlinks'
matchedlinks = root.cssselect("li p a")
#print that
print(matchedlinks)
```

Save the changes to your code, and run it to check that it works.

It will take a while to print the full webpage (you may want to comment out that print command so it doesn't take so long next time). The final line will be a very long list of elements that look like this:

`<Element a at 0x7fd8d69ed310>`

Each one will be separated by a comma, and you may notice right at the end a square bracket.

This is because `matchedlinks` is a **list**: it starts and ends with a square bracket, and each item in that list is separated by a comma.

It's a very long list, too, because there are lots of matches for the pattern identified by the CSS selector.

At the moment each item doesn't make much sense: we need to convert each item back to something that makes sense.

To do something with each item, we need to *loop through* that list and deal with each item in turn.

## Looping through the list

At this point we have to add some completely new code that isn't in the template. Here it is:

```py
#Loop through the items in matchedlinks, calling each one li
for li in matchedlinks:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  #print that
  print(listtext)
```

The comments explain what those lines do. The function `.text_content()` converts that confusing code `<Element a at 0x7fd8d69ed310>` into something more readable and useful: the text contents of the tag that was grabbed.

We store that text in a variable, and then print it.

Before running this code it's a good idea to now *comment out* a couple of the other `print()` commands which you don't need to see anymore and which take up unnecessary time. Those are:

`#print(matchedlinks)`

And:

`#print(html)`

Save your changes and run the code. It should print out a lot of text - but then hit an error. We'll solve that later. But the main thing is that this works on most of the page - we've scraped a whole bunch of data. Now we need to get it out...

## Saving the scraped data

Data is often stored in a type of variable called a **dictionary**. A dictionary consists of a series of pairs (called *key-value pairs*) like so: `"name":"Paul"`. Those pairs are separated by commas and placed inside curly brackets like so: `{ "name":"Paul", "Age" : 23 }`.

You can see how it suits data well - it's like a row in a table.

We need to save the data in two stages:

1. First, we need to store each part of data in a dictionary variable under some sort of *key*, like 'address';
2. Second, we need to store each dictionary in a table, one 'row' (dictionary) at a time.

To store the data in a dictionary, we need to first create it. That line of code is added *before* the list in the first line of code below:

```py
#create a dictionary called record
record = {}
#Loop through the items in matchedlinks, calling each one li
for li in matchedlinks:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  #print that
  print(listtext)
```

That code `record = {}` creates an *empty* dictionary.

Next, we add a line *within* the loop which stores some information inside that dictionary, meaning it is no longer empty.

```py
#create a dictionary called record
record = {}
#Loop through the items in matchedlinks, calling each one li
for li in matchedlinks:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  #print that
  print(listtext)
  record['address'] = listtext
```

The `['address']` bit in `record['address'] = listtext` creates a *key* in that empty dictionary (think of it as a column header). Whatever `listtext` is, is then stored against that key (think of it as being put in that column).

So now we've stored the data in the dictionary, we need to save it to a table. For that we need another line: `scraperwiki.sqlite.save(['address'],record)`.

This saves `record` (the dictionary) to a sqlite database. To do that it needs to specify a *unique key* - remember that a key in a dictionary is like a column in a table, so a 'unique key' is like saying 'a column where every value is unique'. We know that each address shouldn't appear more than once (although could a property be auctioned twice?) so we use that.

This is added inside the loop, too, like so:

```py
#create a dictionary called record
record = {}
#Loop through the items in matchedlinks, calling each one li
for li in matchedlinks:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  #print that
  print(listtext)
  record['address'] = listtext
  scraperwiki.sqlite.save(['address'],record)
```

Once you've written this code once, you can re-use it again, adapting it slightly (or more) for each situation.

## Troubleshooting a bug

### Notes: creating a variable

A first thing to highlight here is the equals operator: `=`

This means that a **variable** is being created or changed. The variable comes before the `=` - in this case the variable is being called 'html'. That makes sense because we are storing a bunch of HTML from a webpage. But the name is arbitrary: you could call it 'thewebpage' or 'allthehtml' or 'donkeyspit'. The main things to remember when creating variables are:

* You cannot have spaces or punctuation in a name: any space will be treated as the end of one name and the beginning of the next. You can use underscores, however, so "all_the_html" is fine but "all the html" is not.
* You cannot use 'reserved' words like `print` or `import` or `list` so try to make your variable names specific.
* If you change the name in one place, remember to change it anywhere else it is used, and spell it consistently. For this reason it's best to use all lower case letters in variable names, so you don't have to remember capitals.

### Notes: creating an lxml.html 'object'

The code `root = lxml.html.fromstring(html)` converts the variable `html` from just a string of characters (HTML code) into something that can be drilled down into: an lxml.html 'object' which is called 'root' here but again could be called almost anything we want.
