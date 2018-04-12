# Cleaning data using Open Refine

This tutorial explains a number of ways you can use Open Refine to clean dirty data. 

First, [download and install Open Refine from the official website](http://openrefine.org/download.html). Open it up - it should open in a browser at http://127.0.0.1:3333/ - this is like an address pointing at your own computer rather than the web: you do not need to be connected to the internet to use it.

## 'Common transforms': basic data problems

The most basic data problems include double spaces, unnecessary spaces at the start and end of data entries, inconsistent capitalisation, and formatting. 

1. [Download this sample dirty dataset](https://docs.google.com/spreadsheets/d/1CDWBeqpUTBd1TkmDz_M6UGRWdHgU7LOcoiGRTvIttKA/edit?usp=sharing#gid=0)
2. [Use it with this tutorial on Open Refine's 'common transforms' features](https://onlinejournalismblog.com/2011/07/05/cleaning-data-using-google-refine-a-quick-guide-2/)

## Data importing: XML and JSON

Open Refine is one of the easiest ways to import and convert data from formats like XML and JSON into a spreadsheet you can analyse using Excel or Google Sheets.

1. Find some data for your area on the [Food Hygiene rating data API page](http://ratings.food.gov.uk/open-data/) - this will be in XML format
2. [Follow the tutorial I've written on the Online Journalism Blog here](https://onlinejournalismblog.com/2015/10/21/how-to-convert-xml-or-json-into-spreadsheets-using-open-refine/)

For a JSON example look for a petition of interest on the [UK Government's petitions website](https://petition.parliament.uk/petitions). Click on the petition page. At the bottom of each petition page should be a link to *Get petition data (json format)* - you can copy the URL for that page and use it to import the data into Open Refine in the same way.

## 'Clustering': fixing misspellings of the same thing

Food hygiene data is a particularly good example to demonstrate another feature of Open Refine.

Like a lot of data, the food hygiene data isn't as consistent as it could be: sometimes McDonalds has an apostrophe, sometimes not; sometimes it's WHSmith, sometimes W H Smith, and sometimes WH Smith. If you're trying to find out how many takeaways there are, your pivot table will be treating each of those as separate entities.

Open Refine has a built-in method for detecting entries that are similar enough that there's a good chance it's just a different spelling of the same thing: it's called clustering. Here's how to do it.

1. Follow the steps above to import the XML data for food hygiene inspections for a particular area: Birmingham's is the URL `http://ratings.food.gov.uk/OpenDataFiles/FHRS402en-GB.xml`
2. Once the project has been created, click on the downward arrow at the top of the *Establishment Detail - Business Name* column (it's normally the 6th column, after the rating out of 5). Select **Edit cells > Cluster and edit...**
3. A new window will appear showing you entries which are *different but very similar*. For example: Nandos, Nando's (with an apostrophe) and Nando'S (with a capital S). To make any cluster of similar entries all the same, tick the box next to each cluster where you are confident they *are* the same (for example Balti Spice and Spice Balti may be different businesses so you would leave that unticked), and then click the button at the bottom marked **Merge Selected & Re-Cluster**. (Tip: if you want to select most of them, it's probably easier to click **Select All** first, and deselect the few that aren't right.)
4. At this point it's worth knowing that what you were seeing was only one *type* of similarity - a particular clustering *algorithm*. Now you can try out a different one by selecting the *Keying Function* drop-down menu and choosing the next one: **ngram fingerprint**. Then, once again, tick the clusters you want to make consistent, and merge them as before. 
5. Repeat this process for the other two algorithms under *Keying Function*: metaphone3 and cologne-phonetic. 
6. That's 4 algorithms used - but there are another two. To access these, click on the *Method* drop-down menu to the left and switch from key collision to **nearest neighbour**. Wait for the clusters to appear and merge the ones that need fixing. For the final algorithm, change the *Distance Function* dropdown menu to **PPM**, and merge the ones that it gets right. 
7. Click **Close** to finish. 

You can now export the results and analyse them in Excel.

## Data combination: importing

Another problem which Open Refine can come in handy for is combining multiple files, or multiple sheets within a single file (e.g. sheets within a spreadsheet workbook).

1. [Download the data on 'disposals' for youth offenders in this folder](https://github.com/paulbradshaw/MED7369-Specialist-Investigative-Journalism/blob/master/cleaning/Disposals%20by%20region%202012-13%20Table.xls). This comes from the youth offending data for 2012/13](https://www.gov.uk/government/statistics/youth-justice-statistics) - specifically the [Regional tables - 2013](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/286086/regional-tables-2013.zip), which also contains other data such as the crimes committed.
2. Launch Open Refine and click on **Create project**
3. Click the **Choose files** button and locate the spreadsheet you downloaded. Click **Next**.
4. You will be taken to a preview screen. Look at the settings in the bottom half - there should be an area towards the middle-right that says *Worksheets to import*. Tick all boxes for all the sheets you want to import.

At this point you *could* click **Create project** in the upper right corner - but there are other data cleaning problems you can address here too...

## Dealing with headings in multiple rows and empty rows: importing

The same preview screen allows you to correct other problems in the data...

1. First, empty rows. *Untick* the box on the right that says *Store blank rows* to correct this.
2. Second: headings in multiple columns! To correct that, look for the box in the middle marked *Parse next 1 line(s) as column header. You'll notice that the `1` can be edited to a different number. Look at your data to see how many rows contain the headings. If it's 2 then change it to `2`. 
3. Note: another option is to ignore the first row altogether, which you can do by ticking the box above marked *Ignore first 0 line(s) at beginning of file*
3. Now click **Create project** in the upper right corner

You will now be taken to your project where you can do further cleaning, or **Export** the data as a CSV or Excel file, among other formats.

For more on this see [How to: clean up spreadsheet headings that run across multiple rows using Open Refine](https://onlinejournalismblog.com/2013/11/13/how-to-clean-up-spreadsheet-headings-that-run-across-multiple-rows-using-open-refine/)

## Faceting: different data in the same column

The youth offending data has another problem common to data: one column actually has 3 different types of data in it. If you open the spreadsheet separately you should be able to see this more clearly:

* First, we have the *geographical area*, such as 'National', or 'East Midlands', or 'Derby' - this is coloured blue in the spreadsheet, but computers can't see colours.
* Second, underneath that, is a *category*, such as 'Pre-court' or 'First tier'. This is bold in the spreadsheet, but again computers can't distiguish that.
* Third, and making up most of the data, is a *specific action*, such as 'Reprimand' or 'Final Warning'.

Really we want a different column for each - this way we could filter based on particular regions or treatments, or categories, and also avoid double-counting (Derby figures are counted again in East Midlands, which is counted again in National ones). 

Open Refine's faceting feature is a very useful way of doing this. It allows you to filter by particular qualities of data, so you can then copy the matching information (just the geographical data, or categories, for example) into new columns. 

### Different types of facets

Before we begin using it properly, it's worth exploring a little to see how faceting works. 

Faceting basically means *grouping and filtering* the data based on qualities in a particular column. For example:

* A *text facet* will show you a list of all the different text entries (e.g. category or business names) in a particular column, and how many times each one appears. You can then filter down to particular ones. 
* A *numeric facet* will show you the range of numbers in a column - typically as a histogram - you can then filter to those within a particular range
* A *timeline facet* will show you the range of dates or times in a column (if it uses them) - you can then filter to those within a particular range
* A *custom text facet* allows you to facet based on a particular property, such as the length of text, the first or last characters, whether it contains a character or not (true or false), and so on.
* A *facet by blank* allows you to filter to just look at cells that are blank (true) or not (false)

As with other functionality in Open Refine, you create a facet by clicking on the downward arrow at the top of the column you want to facet on. Try a couple first to get the idea:

* With the menu open for the first text column, select **Facet > Text facet**. You should now see on the left hand side a box showing the terms that appear in that column - you can order alphabetically or by count (a number in grey next to each phrase indicates how many times it appears). If you click on any entry it will show only those records that match - note that the heading will change to *11 matching record (277 total)* or something similar when this is applied. Close the facet by clicking the x button in the upper right corner of the facet box, or you can click 'reset' to cancel your selection.
* With the menu open for the first numeric column, select **Facet > Numeric facet**. You should now see on the left hand side a box with a histogram showing the range of values. Click and drag the slider to narrow the range being shown. Then close the facet.

Now you've got used to it, let's try to apply that to our problem. Here's how to do it:

1. Take a look at the data and try to identify what distinguishes each piece of information: what is the difference between the rows that show specific actions, and those which just describe the category or region? Don't just look at the one column - look at the columns next to it. Spend a few minutes thinking about that before continuing...
2. Struggling? OK, here are some things to think about: Do the cells or their neighbours have numbers or text? Do they start or end with particular types of characters? Are they of significantly different lengths? Do they include specific characters such as semi-colons, punctuation etc? Are neighbouring cells always empty or full? That last one was a big clue...
3. You already have your data in Open Refine. Now click on the arrow at the top of the column which contains the data *you want to differentiate on*. In this case, that is the column titled 'Age 10-14'. Why? Because this column is *always empty when it's a region or category, and only has numbers when the row is for specific data*.
4. With the menu open for that column, select **Facet > Customized facets > facet by blank**. You should now see on the left hand side a facet box showing 'true' (blank) or 'false' (not blank). Click 'false' to only select those records with numbers in that column.
5. Now, we are only seeing the rows that refer to the sort of disposal that was issued. We need a new column to store the description for these rows only. To do that, select the arrow at the top of the column we want to copy from - the first text column. And then select **Edit column > Add column based on this column...**
6. A window will appear. In *New column name* at the top, call it 'disposal'. Leave everything else as it is - it will copy the *value* of the column you selected into a new column. Click **OK**.
7. You should now see the new column. That's one part of our problem solved. Next we need to separate out the geographical, and categorical, data. Again, to do this we need to think about how those are different. 
8. First, you need to remember that you are still looking at a facet - rows where the 10-14 column is not blank (false). Now click on 'true' to switch to those where it is blank - the categories and geography. It might not be obvious from this, but one difference between the regions and the categories is frequency: the regions only appear once, but the categories appear multiple times - 11 in fact: one for each region. To facet on that basis we can create a text facet on the first column. So, do that (see above if you need a reminder).
8. You should now have a facet box appear on the left. It will be sorted by name, but click **count** in that box to bring the most common values to the top. 
9. Three should appear 11 times: Custody, First-tier and Pre-court. Select **Custody** and you should now see those 11 matching records. Now, still in your facet area *hover over* **First-tier** and you should see the option to **include** - click that. Those 11 records will now be included in the facet alongside the other 11, making 22 in total. Repeat this with **Pre-court**: hover over it so you see the option to **include**, click it so that you have 33. Now, if you've got the original spreadsheet open you might notice that there are actually 4 categories - the other is *Community*. This only appears 6 times, presumably because it wasn't used in all regions. But you need to **include** this also before you continue.
10. With all those selected you can copy them across to a new column as before. Call this column *Category*.
11. One more column to go. Back in your text facet, click **reset** to return to the 61 matching records that you had (the facet by blanks is still applied, in the box above). Now you can manually select all the regions and copy *those* across to a new column in exactly the same way (don't worry about the footnotes and other stray entries). There is a better way to do this but it's overly complicated for the purposes of what we're exploring here.
12. After all that you should now have a dataset with 3 new columns: region, category, and disposal. The final step is to copy two of those down so that our disposal rows *also* have the relevant category and region data. To do that, first close all your facets so that you are looking at all the data. Next, click on the down arrow at the top of the region column and select **Edit cells > Fill down**. This will copy each region down wherever there are blank cells underneath.
13. Repeat this process with the category column.
14. Now you have all the data together and separated appropriately. There's no need to copy down the disposal column - in fact if you wanted to be really tidy you could always remove the rows where there's no disposal data and only the remains of the now unneeded region and category data. But again, it's not necessary so I'm not going to get bogged down in it here.


## Examples

* Tony Hirst explains [Data Shaping in Google Refine – Generating New Rows from Multiple Values in a Single Column](https://onlinejournalismblog.com/2012/07/30/data-shaping-in-google-refine-generating-new-rows-from-multiple-values-in-a-single-column/)
* I've written about [Scraping data with Google Refine](https://onlinejournalismblog.com/2012/01/13/sftw-scraping-data-with-google-refine/)
* Ion Mates explains how he used some of Refine's more advanced functionality, and regex, in his post on [cleaning a converted PDF](https://onlinejournalismblog.com/2015/04/07/how-to-clean-a-converted-pdf-using-open-refine/)
* Cristian Giuletti explains [How to: combine multiple rows in a dataset where text is split across them](https://onlinejournalismblog.com/2014/05/30/how-to-combine-multiple-rows-in-a-dataset-where-text-is-split-across-them-open-refine/)
* More at https://onlinejournalismblog.com/tag/google-refine/page/2/
