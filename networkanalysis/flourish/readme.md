# Creating a network analysis in Flourish

The data visualisation tool Flourish [allows you to create a network graph](https://app.flourish.studio/@flourish/network-graph). Here's how to get started with creating network analysis.

## Find the network graph in Flourish

You can create a network graph in Flourish by going to the ['New visualisation' page](https://app.flourish.studio/templates) and searching the page (use CTRL+F) for 'network'. The charts you are looking for are in a section called **Network graph** quite low down the page. 

There are three options - or 'starting points' - in that Network graph section:

* Default
* Directional
* With images

Actually, all of these are the same chart, with the only difference being that each one has slightly different example data which shows you how to achieve different effects. 

We will start with the basic 'Default' network graph, which can also be found [on Flourish's dedicated network graph page](https://app.flourish.studio/@flourish/network-graph).

## Look at the example data

Once you have clicked on the button to create a network graph in Flourish, go to the *Data* view to see what sort of shape the example data has.

The first thing to highlight is that a network graph on Flourish needs *two* tables (this is quite common):

* Links
* Points

You will need to make sure that your data is formatted in the same way. Specifically:

The **Links** data should show the connections by having a column for the 'source' of each connection, and a column for the 'target'. You can also have a third column showing the 'value' of that connection: for example, if you are showing payments, the value could be the amount of money in each payment from a source to a target. If you were showing relationships in a sports team, the value could be the number of passes from a source to a target. The value can be used to determine the thickness of each connection in the network.

The **Points** data should show the names of each entity mentioned in the Links data. The difference is that these names *only appear once* in this dataset, whereas in the Links data the same entity can appear multiple times, in different connections. You can also have a second column showing the 'group' that each entity belongs to (this can be used to colour code nodes in the diagram), and a third column showing a 'value' (this can be used to size the nodes). Further columns can be used for any information you want to have pop up when someone hovers over a node (for example a description) and a link to any image.

## Get some data showing nodes and connections

I've created a dataset which follows that pattern, which [you can see here](https://docs.google.com/spreadsheets/d/e/2PACX-1vSznt7Jqd0R6FgCxSIpwa55e9LwxOOFX6XkwEU5UXLqoNDR808zw4U5Rp-sp2IIBwjL1WFDkc6s3SlO/pubhtml).

Download the data from that link. We are going to use that data for this tutorial.

When you come to use your own data, here is a tip for getting it into the right shape:

*Tip: if you only have data for links, you can generate a points dataset by, first, creating a pivot table which shows each 'source' once. Then, second, creating a second pivot table to show each 'target' once. And then, third, combining the two lists (you may need to remove any duplicates which appear as both sources as targets). You can even use the pivot tables to count or sum values connected to each entity so that those totals can be used to size each node.*

## Replace the data in the 'Links' table

Making sure that you are still in the **Data** view of your network graph on Flourish, select all of the data in the 'Links' tab, and delete it.

You can now replace it with your own data: this should be the first sheet in the data linked above, called 'StarWarsNetworkWithTimes'.

You can either copy from the spreadsheet and paste directly into Flourish - or you can upload it using the *Upload data* button to the right of the table in Flourish.

## Replace the data in the 'Points' table

Now switch to the 'Points' tab, and again delete all the example data that's there. 

This time, copy (or upload) the data from the second sheet in our own data, 'nodeslist'. 

You should see the preview in the lower right corner update to reflect the new data. But it's a bit of a mess - let's fix that.

## Specify which columns you want to use for the graph

Still in the 'Points' tab, look at the settings on the right hand side, where it says *Select columns to visualise*.

* `ID` is used to specify which column has the names of your entities - these should match the names in the other table. This is column A.
* `Group` is used to colour-code your nodes, if you want to. In our case, we want to colour each node based on whether it is a film or a character. That information is in column C, so change that box to say C. This solves our messy chart as before it was colouring ever node differently. (If you don't want any different colours, leave this box empty)
* `Size` can be used to specify a column for sizing each node. Type B in this box, as we can use the total time for each character or movie as a way of doing this.
* `Image` can be used to specify a column with URLs for images - we don't have one (but you could create one!)
* `Info for popups` specifies any column(s) whose information you want to be able to access for popups. We'd like all of them, please! So change this to A-Ca

