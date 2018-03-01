# Network analysis

This folder contains resources for doing a network analysis. Network analysis can be useful both in planning investigations (mapping networks and identifying actors within that) and storytelling (showing patterns or allowing users to explore networks).

## Exercise: a network analysis of characters in Star Wars

One of the easiest tools to get started with network analysis is Google Fusion Tables. This is best known for mapping, but it also allows you to create a network graph. In this repo you will find some data showing the relationships between characters and films (who appeared in what, for how long). These can be used to create a network graph [like this](https://fusiontables.googleusercontent.com/embedviz?containerId=googft-gviz-canvas&viz=GVIZ&t=GRAPH&gc=true&gd=true&sdb=1&rmax=100000&q=select+col0,+col1,+col2+from+1zYTCsra3gSDmmqKgLPqsT0KQlkGD2OSY71TOU9bQ&qrs=+where+col0+%3E%3D+&qre=+and+col0+%3C%3D+&qe&uiversion=2&state=%7B%22ps%22:%221_0_2p_0_5_2_-p_6_i_-1f_4_-e_m_a_-1i_-1q_3_16_1d_1_15_-8_d_-13_-h_2_1u_z_b_-p_-12_e_-2b_2a_f_c_3_8_1j_b_c_2n_18_k_11_l_9_-h_-6_h_-g_-1v_g_19_-t_p_3d_j_q_-2e_-1w_j_-1q_-2l_r_3_-1y_l_-2s_2u_t_-31_24_m_3a_-p_v_-23_-2b_u_25_1u_10_-1b_1g_z_-2a_-1e_11_-29_31_i_2c_-p_s_26_1f_14_3j_-e_x_3m_-1_15_14_-25_17_-34_2k_18_14_29_16_-6_1w_19_3e_v_1b_a_1j_1e_1t_1z_1d_-32_1p_1f_2m_1s_1c_j_t_1h_-2e_-2e_1g_d_1w_1i_w_-2g_1k_-2m_-1i_1n_3x_5_1m_m_-2m_1p_1f_-27_1q_24_26_1s_2g_23_1r_-18_-18_1l_9_n_1j_-22_10_1w_3u_-o_1v_-3k_2k_1u_-1u_18_22_16_-2u_20_-2y_-1v_21_-2u_-2b_23_45_-6_25_2p_2a_28_-1e_1_27_-3v_2c_26_47_-i_29_-19_8_24_1i_-2n_12_34_25_2a_1f_31_2b_-3z_1z_n_-45_-1w_o_-57_21_1t_4h_2h_w_-5s_27_y_-5m_18_13_-5r_1p_1a_65_-h_1o_66_7_7_46_-1z_1y_-r_3a_1x_-4z_-1n_1z_59_1p_2c_-3w_k_%22,%22cx%22:20.18904830628475,%22cy%22:-0.21896961370335616,%22sw%22:985.6943560771015,%22sh%22:330.25841827325564,%22z%22:1.2466226231977893%7D&gco_forceIFrame=true&gco_hasLabelsColumn=true&width=1000&height=600).

You can also [access the entire Google Fusion Table - Star Wars network with times - here](https://www.google.com/fusiontables/DataSource?docid=1zYTCsra3gSDmmqKgLPqsT0KQlkGD2OSY71TOU9bQ)

Note the structure of the data: one table with three columns:

* 'From' entity
* 'To' entity
* Quantitative dimension (e.g. money, time, amount)

In other network analysis this structure may be separated across two separate datasets, as detailed below with Kumu.

### What to do

* First you need some data to visualise. You can [find that here](https://raw.githubusercontent.com/paulbradshaw/MED7369-Specialist-Investigative-Journalism/master/networkanalysis/StarWarsNetworkWithTimes.csv) - save it to your computer by pressing CTRL+S (CMD+S on a Mac) or selecting *File>Save* in your browser menu.
* In Google Drive create a new Fusion Table by going to *New > More*. If you already have Fusion Tables installed you can select it here; otherwise select *Connect more apps* and find it in the Google Drive app store. Once connected, it will be added to the 'more' menu for next time. Alternatively, you can access Fusion Tables directly at https://fusiontables.google.com/.
* Upload the data you want to visualise
* Click on the red plus sign (next to the last tab) and select *Add chart*
* On the menu that appears, scroll to the bottom and choose the network graph option
* Configure the options to choose which column is 'from' (film) and which is 'to' (name). Form *Weight by* choose the numerical column ('As time'). You can also tick 'color by columns' so you can tell the films from the names.
* That's it. Once done you can now publish your chart by clicking the drop-down menu on the tab and selecting *Publish*. Change the width and height in the code to make a bigger window.



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

### Customising a network diagram in Kumu: tutorial

I've [put together a tutorial explaining how to colour code elements in Kumu, and also how to analyse it to identify numbers of connections](https://docs.google.com/document/d/e/2PACX-1vTQVZsPzYX0u-FtCrpWpO7G8nCO35UMoZuQX-T4x7m5P633IV7D28ThsFVg2ptkVvztoaJVcpR8Hd2G/pub)

## Advanced network analysis: neo4j and the Panama Papers

The Panama Papers investigation used the powerful tool **neo4j** to analyse relationships. If you're interested in that particular dataset, or neo4j more generally, I've written some [notes on using the Panama Papers database with neo4j here](https://github.com/paulbradshaw/MED7369-Specialist-Investigative-Journalism/blob/master/networkanalysis/neo4j.md)

## Links and other resources

You can find [my bookmarks on various things related to network analysis here](https://pinboard.in/u:paulbradshaw/t:networkanalysis). Add extra tags to drill down further, e.g. [https://pinboard.in/u:paulbradshaw/t:networkanalysis+tools](https://pinboard.in/u:paulbradshaw/t:networkanalysis+tools) shows tools that I have bookmarked.
