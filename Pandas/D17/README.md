# D17: Pandas Efficiency Optimize

After know pandas and know how to deal with many kinds of data form, we ask for high effciency. There are three way for optimizing the executed time:<br>
	a. read and write file<br>
	b. use built in functions<br>
	c. deal with vector data

* * *
*	read and write file: compare to reading csv file, we can see that each type of file relative to their loading speed:<br>

| File format | running time | Speed |
| :---------: | :----------: | :---: |
| xlsx | 1min 19s +- 2.82s | ignore |
| csv | 581ms +- 16.6ms | 1 |
| pkl | 98.4ms +- 1.9ms | 5.90 |
| hdf | 120ms +- 1.79ms | 4.84 |

from the form, we can see that the fastest is loading pkl files, so when we can choose to write data form in pkl files as possible.<br>

*	use built in functions: when we use `.agg()` or `.transform()` function, we should use built-in functions instead of self-defined functions for decreasing running time. But if we can't avoid to use self-defined functions, we should choose agg rather than transform.

```
>>> start_time = time.time()
>>> score_df.groupby('class').agg('mean')
>>> end_time = time.time()
>>> end_time - start_time
0.0032
>>> start_time = time.time()
>>> score_df.groupby('class').agg(lambda x: x.mean())
>>> end_time = time.time()
>>> end_time - start_time
0.017
>>> start_time = time.time()
>>> score_df.groupby('class').transform('mean')
>>> end_time = time.time()
>>> end_time - start_time
0.020
>>> start_time = time.time()
>>> score_df.groupby('class').transform(lambda x: x.mean())
>>> end_time = time.time()
>>> end_time - start_time
0.027
```

*	when we use `.isin()`, we can select or find the data very fast compare with logical decision or `.apply()`. the pros of .isin() is that we can compare two dataframe, but it depends. [how to use .isin()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html)

* * *
*	Dealing with Big Data: we usually have insufficient memory problem when facing to big data, and that cause lower speed, so we can try to decrease the data type level to save memory.<br>
Let's generate two big data frames first: (unit=bytes)
```
>>> float_data = pd.DataFrame(np.random.uniform(0, 5, 1000000).reshape(1000,100))
>>> int_data = pd.DataFrame(np.random.randint(0, 1000, 1000000).reshape(1000,100))
>>> float_data.memory_usage(deep=True).sum(), int_data.memory_usage(deep=True).sum()
(800128, 800128)
```
we can change int into uint type to save memory.(int64 -> uint16):
```
>>> downcast_int = int_data.apply(pd.to_numeric, downcast='unsigned')
>>> int_data.memory_usage(deep=True).sum(), downcast_int.memory_usage().sum()
(800128, 200128)
```
the reason that it can save memory is because there are 100 int64 downcast to uint16.
```
>>> compare_int = pd.concat([int_data.dtypes, downcast_int.dtypes], axis=1)
>>> compare_int.columns = ['before', 'after']
>>> compare_int.apply(pd.value_counts)
```

|     | before | after |
| :-: | :----: | :---: |
| uint16 | NaN | 100.0 |
| int64 | 100.0 | NaN |

we can also downcast float64 into float32, and we can save half of float64 memory. The way is same as above.












