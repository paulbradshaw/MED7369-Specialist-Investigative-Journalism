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

## Clustering

