# Network analysis

This folder contains resources for doing a network analysis. Network analysis can be useful both in planning investigations (mapping networks and identifying actors within that) and storytelling (showing patterns or allowing users to explore networks).

## Exercise: manual network analysis using Kumu

[Kumu.io](https://kumu.io/) is a tool for creating network graphs and similar data visualisation. These can be generated from datasets, or created manually. 

Once created, data can also be exported, which is a good way of getting used to how network analysis is typically structured. This time the data is split across two separate datasets, which are then combined in analysis. Those datasets are *entities* and *relationships*:

**Dataset A: Entities/nodes/elements**

This dataset just lists the entities involved in the network. They must include a name field, but there can be as many other fields as possible. For example:

* Name/label
* Type (sometimes used to colour code the node)
* Image URL (this can be used to illustrate the node)
* Description/address/URL etc. (used for labels)
* Tags (used for filtering or other functionality)

**Dataset B: Relationships/connections**

The second dataset details the relationship between those entities. Here is a typical structure:

* Entity 1/from
* Entity 2/to
* Direction of relationship (e.g. from 1->2 or vice versa)
* Type of relationship (e.g. parent-child, sibling, director-company, client-company, employer-employee, partner, shareholding etc.)
* Quantitative dimension (e.g. number of shares, amount of money, period of time, etc.)
* Description (for labelling)
* Tags (used for filtering or other functionality)

### What to do

Create a simple network using Kumu. Choose the **Stakeholder** option to show a network. The **Sytem** option can be used to show flows and systems: for example the connections are typically arrows showing movement from one part to another (you can find other flow chart-style options in **Other**). The **SNA** (Social Network Analysis) option is best for large datasets with thousands of connections, and can show clusters, cliques, and outliers. 

* Click on the plus icon at the bottom and select 'Sketch'. This is the easiest way to create nodes and connect them.
* Click on the canvas to add a node, then name it. Add a few.
* Click and drag from one node to another to connect them. Add a description of the relationship.
* *Making sure you are not on any individual element* (click on the background), export by clicking on the ... (more) option in the bottom right corner. Here you can *Export .xlsx* and also JSON (for use with JavaScript visualisation or R network analysis)
* Look at the spreadsheet you've just exported. It should have 2 sheets: *Elements* and *Connections*. If you want, you can use this template to create the data for a network diagram first, and then import it into a new *empty* Kumu network diagram (otherwise it will be added to any data already present).
* You can also publish and embed your network visualisation from the same menu, or capture a screenshot or PDF

Here's [an example of using the System option to explore the system surrounding homelessness](https://embed.kumu.io/b923cf0c9d464facfba9651df97c8d45#homelessness) - I've added some colour (see below).

### Customising a network diagram in Kumu: tutorial

I've [put together a tutorial explaining how to colour code elements in Kumu, and also how to analyse it to identify numbers of connections](https://docs.google.com/document/d/e/2PACX-1vTQVZsPzYX0u-FtCrpWpO7G8nCO35UMoZuQX-T4x7m5P633IV7D28ThsFVg2ptkVvztoaJVcpR8Hd2G/pub)

[This example adds sizing](https://embed.kumu.io/9d61cc335f508ac6a929793ceff3669a#import) (but doesn't have colour).

## Advanced network analysis: neo4j and the Panama Papers

The Panama Papers investigation used the powerful tool **neo4j** to analyse relationships. If you're interested in that particular dataset, or neo4j more generally, I've written some [notes on using the Panama Papers database with neo4j here](https://github.com/paulbradshaw/MED7369-Specialist-Investigative-Journalism/blob/master/networkanalysis/neo4j.md)

## Links and other resources

You can find [my bookmarks on various things related to network analysis here](https://pinboard.in/u:paulbradshaw/t:networkanalysis). Add extra tags to drill down further, e.g. [https://pinboard.in/u:paulbradshaw/t:networkanalysis+tools](https://pinboard.in/u:paulbradshaw/t:networkanalysis+tools) shows tools that I have bookmarked.
