# Gephi notes

*Notes from a talk by Thomas Ebermann - see [GitHub repo](https://github.com/paulbradshaw/gephi-workshop)*

## Generate a network graph file first

The repo has a Gephi graph file with the extension `.gexf` - `sample.gexf` - which can be used to try out the different functionality.

It also has a file called `scrape_friends.rb` which will scrape your Facebook account for your own connections (you need to edit the file to add your login details) and generate a version for your network.

And the `19714.json` file is network data on passes between players from the StatsBomb API - [details in the PDF](https://github.com/paulbradshaw/gephi-workshop/blob/master/Open%20Data%20Events%20v1.3.0.pdf). The [accompanying Python notebook has script which converts that to a .gexf file](https://github.com/paulbradshaw/gephi-workshop/blob/master/Soccer.ipynb).

Alternatively you can prepare data for Gephi - you can [find instructions on that here](http://humnviz.blogs.bucknell.edu/files/2015/11/Data-Preparation-for-Gephi.pdf). The web-based tool Kumu.io is one way to manually generate data in this structure (nodes and connections in 2 separate CSV files).

Whatever you use, open the file in Gephi.

## Change the layout

On the left of the screen should be a *Layout* area. You can select different options from the drop-down menu to change how the network is displayed.

Try **Yifan Hu** and click **Run**

Change *Optimal Distance* to 300 and run again. This will change the appearance further.

Try other layouts to see the impact. [More about different layouts in this presentation](https://gephi.org/tutorials/gephi-tutorial-layouts.pdf)

## Change the appearance

On the left of the screen should be an *Appearance* area. You can select different aspects in the top right of this area (colour, size, label colour, label size) and top left (nodes or edges) then use the drop-down menu underneath to change for example the colouring of elements based on different factors.

Try selecting *Nodes*, and *Ranking* and then **Degree** from the drop-down. You should see a colour scale appear below, which can be left as-is, or altered using the palette button to the right.

Click **Apply**.

The nodes should now be coloured based on the degrees (numbers) of connections.

### Adding other statistical analyses to guide appearance

On the right of the screen is a *Statistics* window (or use the **Windows** menu to open it).

One of the analyses you can run here is *Avg. Path Length* - click **Run** next to this.

A window should appear with the results. This can be closed.

Now this new measure should be accessible as an option for appearance. First, however, you may need to navigate away from the *Nodes > Ranking* view in order to force a refresh (try selecting *Edges > Ranking* first, and then going back to *Nodes > Ranking* again). Alternatively, and better for this, change from colour to *Size* by using that button (the 3 circles increasing in size next to the palette icon in the upper right of this area).

Once this is done, select the drop-down and now you should be able to see **Betweenness Centrality** (You can google that term to find out more about what it shows) to size (or colour) based on that measure. Change the range of the size so it is between 10 and 80 to see a different effect.

(Once it is 10-80 in size there will be overlaps, so in the *Layout* pane try clicking **Stop** on the current layout and changing to **Noverlap** (**Run**) to avoid this).

#### Communities/modularity

Back in the *Statistics* window, find *Modularity* and click **Run** to run that analysis. This should find groups of 'communities' in the nodes.

To colour-code nodes based on their community, go to the *Appearance* window, select the colour button, then Nodes, Partition, and then from the drop-down select **Modularity Class**. Then **Apply**.

## Adding and changing labels

Across the bottom of the *Graph* window should be a black 'T' among other options. Click this to add text labels.

You can change the font by clicking the button that states the font, e.g. **Arial-BoldMT,32**.

To stop labels overlapping, go to the *Layout* window and select **Label Adjust** then **Run**.

### Sizing labels by node size

To size each label based on the node it is labelling, click on the black 'A' and select **Node size**.

Use the slider to the right to adjust.

## Filters

To add filters go to the *Filters* window. In *Library* you can see various categories of filter.

Select *Topology* and then drag **Degree Range** into the *Queries* area below to use it.

Now click on **Degree Range** and you should see a histogram of the distribution of degrees (of connections) for all nodes. Click and drag the slider to select the range you want to filter to, then click **Filter** to apply.

## Preview

Use the *Preview settings* window - make sure it is big enough to see the options - and click **Refresh** to generate a preview in the *Preview* window. (Open both windows from the **Window** menu)

Check the *Node Labels* section and turn on *Show Labels* to show them in the preview.

Click **Refresh**.

Try other options - and click **Refresh** each time.

Once happy, in the *Preview settings* window click on **Export SVG/PDF/PNG** and select the format you want and where you want to export it to.

## Other datasets to try

- http://snap.stanford.edu/data/
- http://cdg.columbia.edu/cdg/datasets
- https://github.com/iKhaled/MCFCAnalytics
