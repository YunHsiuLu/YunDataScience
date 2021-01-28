# D12: Pandas Common Charts Design

There are many common charts when representing the statistical results: line graph, pie chart, bar chart, histogram, box chart, scatter graph, density graph, high density scatter graph, area graph, etc.

* * *

*	Line Chart: Line chart can show the data trend, we can easily plot line chart in pandas with `DataFrame.plot()`. If there are several columns, they will show on the plot at the same time.<br>
Warning that if you are not using jupyter notebook and want to show the plot, you need to use matplotlib to show.

*	Pie Chart: or call circle graph. Pie chart can show the ratio of different part clearly. The way to plot pie chart is using `DataFrame.plot.pie()`

*	Bar Chart: it can show independent data. `DataFrame.plot.bar()`

*	Box Chart: it can easily show the mean of data and the interval of discrete data. `DataFrame().boxplot()`

*	Scatter Graph: it can show the trend of correlated data. `DataFrame.plot.scatter()`