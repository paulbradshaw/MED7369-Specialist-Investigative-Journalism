# Tableau tutorial: food hygiene data dashboard

This tutorial uses food hygiene data to explore the creation of charts, and then a dashboard, in Tableau Public.

First, [download the Tableau Public app](https://public.tableau.com/) if you haven't already. This is the free version of Tableau Desktop, although as a student you can also download Tableau Desktop and get access to private data and other features if you want.

## Importing data - splitting columns

Import data into Tableau - it will open in a tab marked *Data Source* which you can return to at any time.

Scroll to the left until you see the postcode column.

Click on the dropdown menu at the top of that column and select **Custom split...**

A new window should appear asking how you want to split it. Type a space to separate the postcodes by the space, and leave the setting underneath as *Split off First 1 columns*.

You should now have a new column containing just the first part of the postcode, before the space. Tableau has the shapes for postcode districts, or outcodes, so you can use this new column to create a choropleth map later, explained below.

To make it easier to find, click on the dropdown menu at the top of that new column and select **Rename**, then give it the name 'outcode'.

While you're at it you might want to rename the most useful columns such as postcode, business name, type, and rating.

## Creating a bar chart

Go to Sheet 1, which has already been created.

On the left you should see a list of *Dimensions* (such as business name, type, postcode, etc.) and *Measures* (numerical columns such as hygiene rating, and geographical ones such as lat-long).

Click and drag the 'Business type' dimension into the *Columns* box at the top.

Click and drag the 'Number of records' measure into the *Rows* box at the top.

You should now see a bar chart - Tableau has guessed this is the best way to show what you are looking at.

To change it to a column chart, click the *Swap rows and columns* button at the top, or select it from the *Analysis* menu (at the bottom) - or you can do it yourself manually.

At the bottom of the chart under the x axis it says 'Number of records'. Hover over this to see a sort option. Click on that, and the bars will be sorted from largest to smallest.

You've now created your first chart. Double-click on the sheet name to change it to 'bar chart: business types'. Note the title of the chart changes to this too.

Try to repeat this process to create another sheet with a bar chart showing number of establishments by business name (in other words which food chain has most outlets in Birmingham!)


## Creating a choropleth map

Next to the first sheet tab at the bottom should be a button to create a new sheet. Click it.

On the left, double-click on the dimension 'outcode' that you created earlier. This should have a little globe next to it, indicating that it has been recognised as geographical data.

A map should appear in the main chart area. On it will be a point for every area covered by the data.

To change these to shapes, we need to specify a colour for each area.

Click and drag the measure 'Number of records' onto the *Color* box in the Marks area between the chart and the list of measures and dimensions.

The map should now change to a series of postcode area shapes, coloured based on the number of records in each area.

Double-click on the sheet name to change it to 'map: businesses per postcode district'. Note the title of the chart changes to this too.


### Creating a point-based map or other type of map

There are lots of other types of map you can make. You can [find more details on how to create a point-based map on Tableau's website](https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_howto_pointdistribution.html). This is part of a [list of map-related tutorials](https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_build.html)

## Creating a heat map

Next to the last sheet at the bottom should be a button to create a new sheet. Click it.

Drag the 'business type' dimension into the *rows* area.

Drag the 'rating value' measure into the *columns* area.

Notice what happens: you get a bar chart. This is because 'rating value' is a number, and Tableau assumes you want to add up all the numbers in that. The chart shows the total of all those ratings added up for each type of business.

But we don't want it to do that. We want to split up the different ratings and count those up.

We need to convert 'rating value' from a measure to a dimension, so it doesn't treat them as numbers to add up but rather as the *categories* they actually are.

Drag 'rating value' out of your columns area, and in the dimensions box hover over 'rating value'. Click the dropdown menu for that dimension.

A menu should appear with various options. One of these is **Convert to dimension**. Click that.

Now 'rating value' should appear in the Dimensions area. Click and drag it into columns.

Now instead of a bar chart you should see a table, with ratings across the top and categories down the side. Almost every box in the table is filled with the value `Abc` - we can change that by dragging another value onto the table.

Click and drag 'Number of records' from the measures box onto the middle of the table.

The `Abc`s should now be replaced by the SUM of records for each type-rating combination.

Look under the *Marks* box to the left, too: you'll notice that 'SUM(Number of records)' is in that area, with a 'T' box next to it, indicating that it is being used to determine the text in each cell of the table.

To change this table to a heatmap, click and drag that 'SUM(Number of records)' box onto the *Color* box instead. You should see the table change so that each cell is *coloured* based on that value, instead of text added.

Now you have a heatmap. Double-click on the sheet name to change it to 'heatmap: ratings by business type'.

Note: this is best done when the range of numbers is similar or at least comparable for each category. For example, it would be better to use percentages than whole numbers. In this case because some categories have very few inspections, their heat maps don't really show which categories are doing worst. You can fix this a little by changing the upper limit on the heatmap range: click on the *Color* box and then **Edit colors...**: a window should appear where you can customise the colours used. Click **Advanced** to open up the option to change the start and end points for the colour range. Make the end point lower if most values are under that number anyway and you want the colour to show a narrower range of values within which most values sit.


## Creating a dashboard

Next to the new sheet button at the bottom should be a button to create a new dashboard. Click it.

On the left you should see a list of the other sheets created so far. Above that is a button for *Device preview*. Click that to open a new row across the top of the screen where you can specify you want to see how this looks on a tablet, phone, or desktop - and which model, resolution etc.

Change it to **Phone**.

Click and drag the map sheet onto your canvas.

The legend takes up the right of the screen. To stop it doing this, select it, then click on the dropdown menu on the right, and select **Floating**. Now it should hover over the map.

Click and drag the chart sheet onto your canvas. As you move it you should see different grey areas appear depending on whether it will take up the left half, right half, bottom or top half. When the bottom half turns grey, release the mouse button to drop it there.

Make sure the chart box is still selected - you should see some options on the right including a dropdown menu, and a filter button. Click the filter button to turn *Use as filter* on. This means that when the user clicks on parts of this bar chart it will filter other data.

Click on the map to make the options appear for that. Click the filter button to turn *Use as filter* on for this too.

Test the filter out by clicking on one area of the map - you should see the bar chart underneath change to show the distribution of *just that area*. Click on the area again to deselect it.

Test the bar chart filter by doing the same - click on one bar and the map should change to reflect the numbers of that type in each area. Click on the bar again to deselect it.

Repeat for any other charts, e.g. heatmap etc.

### Examples of food hygiene dashboards

You can [see an example here](https://public.tableau.com/profile/paul.bradshaw#!/vizhome/Birminghamfoodhygieneexample/Dashboard1)

For a much more ambitious example of creating a dashboard for food hygiene data, see Luke Stoughton's dashboard [Food Hygiene Ratings UK - how do your local businesses score?](https://public.tableau.com/profile/luke.stoughton8750#!/vizhome/FoodStandardsRatings/FoodStandards)

Other examples include data journalist [Claire Miller's line chart on food hygiene ratings from 2010-2012](https://public.tableau.com/profile/clairemiller#!/vizhome/FoodHygieneRatings-June2012/Proportionofscores), Chris Love's [correlations between food hygiene and deprivation](https://public.tableau.com/profile/chrisluv#!/vizhome/ExaminingFoodHygieneRatingsbyLocalAuthority/FoodHygienevsIMD) (with worrying potential for p-hacking), or [search Tableau for visualisations using the keywords 'food hygiene'](https://public.tableau.com/en-us/search/all/food%20hygiene)

## Tableau tutorials

There are lots of tutorials on the Tableau website at https://public.tableau.com/en-us/s/resources - as well as around the web.
