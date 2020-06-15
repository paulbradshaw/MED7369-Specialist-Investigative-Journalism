# Exercise: manual network analysis using Kumu

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
