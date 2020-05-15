# Extracting numbers from cells

## Exclude cells that have no numbers in them at all

1. Click on the dropdown menu at the top of the column you want to work with (the one which has mixed descriptions and amounts). Select **Facet > Custom text facet...**
2. A new window will appear where you can enter an expression using GREL (Google Refine Expression Language). Enter this expression: `value.partition(/[0-9]+/)[1]`
3. The preview should show you the results on the right. Click **OK** to apply a facet based on this expression.
4. The new facet will appear on the left hand side of the screen under *Facet/Filter*: it will show you a list of the (first) numbers in each cell in this column. 
5. Scroll to the bottom to see the *(blank)* option. Click once on this and your main data view will change so you only see those with no numbers in that column. 
6. Now, in the *Facet/Filter* area on the right, click on *invert* to invert your selection so it shows all the entries *apart* from those with numbers in that column.

