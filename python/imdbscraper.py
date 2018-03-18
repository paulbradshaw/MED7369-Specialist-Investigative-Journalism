#!/usr/bin/env python


import scraperwiki
import urlparse
import lxml.html
# scrape_table function: gets passed an individual page to scrape
def scrape_table(root):
    rows = root.cssselect("td.titleColumn")  # selects all cells in <td class="titleColumn"
    ref = 0
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
        ref = ref+1
        spans = row.cssselect("span")
        if spans:             
            record['year'] = spans[0].text
            record['ref'] = ref
            # Print out the data we've gathered
            print record, '------------'
            # Finally, save the record to the datastore - 'Artist' is our unique key
            scraperwiki.sqlite.save(['ref'], record)
        
# scrape_and_look_for_next_link function: calls the scrape_table
# function, then hunts for a 'next' link: if one is found, calls itself again
def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
    scrape_table(root)

# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
starting_url = 'http://www.imdb.com/chart/top'
scrape_and_look_for_next_link(starting_url)
