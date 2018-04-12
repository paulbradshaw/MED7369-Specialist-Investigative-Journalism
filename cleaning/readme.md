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

## Fixing misspellings of the same thing: 'Clustering'

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

## Data combination

Another problem which Open Refine can come in handy for is combining multiple files, or multiple sheets within a single file (e.g. sheets within a spreadsheet workbook).

1. [Download the data on 'disposals' for youth offenders in this folder](https://github.com/paulbradshaw/MED7369-Specialist-Investigative-Journalism/blob/master/cleaning/Disposals%20by%20region%202012-13%20Table.xls). This comes from the youth offending data for 2012/13](https://www.gov.uk/government/statistics/youth-justice-statistics) - specifically the [Regional tables - 2013](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/286086/regional-tables-2013.zip), which also contains other data such as the crimes committed.
2. Launch Open Refine and click on **Create project**
3. Click the **Choose files** button and locate the spreadsheet you downloaded. Click **Next**.
4. You will be taken to a preview screen. Look at the settings in the bottom half - there should be an area towards the middle-right that says *Worksheets to import*. Tick all boxes for all the sheets you want to import.

At this point you *could* click **Create project** in the upper right corner - but there are other data cleaning problems you can address here too...

## Dealing with headings in multiple rows and empty rows

The same preview screen allows you to correct other problems in the data...

1. First, empty rows. *Untick* the box on the right that says *Store blank rows* to correct this.
2. Second: headings in multiple columns! To correct that, look for the box in the middle marked *Parse next 1 line(s) as column header. You'll notice that the `1` can be edited to a different number. Look at your data to see how many rows contain the headings. If it's 2 then change it to `2`. 
3. Note: another option is to ignore the first row altogether, which you can do by ticking the box above marked *Ignore first 0 line(s) at beginning of file*
3. Now click **Create project** in the upper right corner

You will now be taken to your project where you can do further cleaning, or **Export** the data as a CSV or Excel file, among other formats.

## Different data in the same column: faceting

The youth offending data has another problem common to data: one column actually has 3 different types of data in it. If you open the spreadsheet separately you should be able to see this more clearly:

* First, we have the *geographical area*, such as 'National', or 'East Midlands', or 'Derby' - this is coloured blue in the spreadsheet, but computers can't see colours.
* Second, underneath that, is a *category*, such as 'Pre-court' or 'First tier'. This is bold in the spreadsheet, but again computers can't distiguish that.
* Third, and making up most of the data, is a *specific action*, such as 'Reprimand' or 'Final Warning'.

Really we want a different column for each - this way we could filter based on particular regions or treatments, or categories, and also avoid double-counting (Derby figures are counted again in East Midlands, which is counted again in National ones). 

Open Refine's faceting feature is a very useful way of doing this. It allows you to filter by particular qualities of data, so you can then copy the matching information (just the geographical data, or categories, for example) into new columns. 

Here's how to do it here:

1. Take a look at the data and try to identify what distinguishes each piece of information: what is the difference between the rows that show specific actions, and those which just describe the category or region? Don't just look at the one column - look at the columns next to it. Spend a few minutes thinking about that before continuing...
2. Struggling? OK, here are some things to think about: Do the cells or their neighbours have numbers or text? Do they start or end with particular types of characters? Are they of significantly different lengths? Do they include specific characters such as semi-colons, punctuation etc? Are neighbouring cells always empty or full? That last one was a big clue...
3. You already have your data in Open Refine. Now click on the arrow at the top of the column which contains the data *you want to differentiate on*. In this case, that is the column titled 'Age 10-14'. Why? Because this column is *always empty when it's a region or category, and only has numbers when the row is for specific data*.
