# Creating a network analysis in Flourish

The data visualisation tool Flourish [allows you to create a network graph](https://app.flourish.studio/@flourish/network-graph). Here's how to get started with creating network analysis.

## Get some data showing nodes and connections

Create a network graph in Flourish and go to the *Data* view to see what sort of shape the data has.

The first thing to highlight is that a network graph on Flourish needs *two* tables (this is quite common):

* Links
* Points

You will need to make sure that your data is formatted in the same way. Specifically:

The **Links** data should show the connections by having a column for the 'source' of each connection, and a column for the 'target'. You can also have a third column showing the 'value' of that connection: for example, if you are showing payments, the value could be the amount of money in each payment from a source to a target. If you were showing relationships in a sports team, the value could be the number of passes from a source to a target. The value can be used to determine the thickness of each connection in the network.

The **Points** data should show the names of each entity mentioned in the Links data. The difference is that these names *only appear once* in this dataset, whereas in the Links data the same entity can appear multiple times, in different connections. You can also have a second column showing the 'group' that each entity belongs to (this can be used to colour code nodes in the diagram), and a third column showing a 'value' (this can be used to size the nodes). Further columns can be used for any information you want to have pop up when someone hovers over a node (for example a description) and a link to any image.
