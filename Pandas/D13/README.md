# D13: Pandas Statistical Function

we can use pandas dataframe to calculate some statistics variable to do some analysis, like mean value, summation, median, etc. Later I will summary some statistical funciton and how to use.<br>
These functions can refer to [D05 lecture](https://github.com/YunHsiuLu/YunDataScience/tree/main/NumPy/D05)<br>

* * *

*	mean(): we can choose one column to get its mean value, be careful that the "column" parameter should not be string.<br>
ex.
```
>>> score_df.mean() #it will list all columns' mean
math_score		60.7
english_score	62.8
chinese_score	63.5
dtype: float64
>>> score_df.math_score.mean()
60.7
```
for another case, we can use for loop to get every column's information (check [D12 exercise](https://github.com/YunHsiuLu/YunDataScience/blob/main/Pandas/D12/D12_exercise.ipynb))<br>
but we can't do as below:<br>
```
for column in df:
	print(df.column.mean())
```
it runs error because column here is a string.<br>
we can also change the axis to get the row mean value. For example, count every students' mean score.<br>
*	sum(): like mean(), we can calculate the column summation or the row summation.
*	count(): we can get row number of one column or every columns. 
*	median(): we can get the median value of one column or every columns.
*	quantile(n): 0< n <1. Get the percent value of one column or every columns.
*	max(), min(): get the maximum or minimum value of one column or every columns.
*	std(), var(): get the standard value or variance of one column or every columns.
*	corr(): get the correlation coefficient between every columns.

* * *

*	apply(): it is very special function rather than numpy statistics, we can self-defined function by `df.apply()` to analyze the data as you want.<br>
ex.
`df.apply(lambda x: x**0.5*10)` means 
```math
f(x) = 10*\sqrt{x}
```

also we have pipe(), applymap() to self-defined function in dataframe [check more](https://data-flair.training/blogs/pandas-function-applications/).












