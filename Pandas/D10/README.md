# D10: Pandas Data Index Operation
this lecture tells how to do data filter, data selection, or data combination.<br>
* * *
*	index:
	*	we can set the index in pandas dataform by `.set_index()`.<br>
	```
	>>> boston_data = pd.read_csv('boston.csv', usecols=['CRIM', 'ZN', 'key', 'INDUS'])
	>>> boston_data_index = boston_data.set_index('key')
	>>> boston_data_index
	```

	| key | CRIM |  ZN | INDUS |
	| :-: | :--: | :-: | :---: |
	| 1 | 0.02731 | 0.0 | 7.07 |
	| 2 | 0.02729 | 0.0 | 7.07 |
	| 3 | 0.03237 | 0.0 | 2.18 |
	| 4 | 0.06905 | 0.0 | 2.18 |
	| 5 | 0.02985 | 0.0 | 2.18 |

	*	we can set the 'layer index' dataform by `.set_index([...])` with an array. <br>
* * *
*	data operation:
	*	rename the column name: use `.rename()` to rename the column.
	```
	>>> new_boston_data = boston_data.rename(columns={'CRIM':'feature1'})
	>>> new_boston_data
	```

	|     | key | feature1 |  ZN | INDUS |
	| :-: | :-: | :--: | :-: | :---: |
	|  0  | 1 | 0.02731 | 0.0 | 7.07 |
	|  1  | 2 | 0.02729 | 0.0 | 7.07 |
	|  2  | 3 | 0.03237 | 0.0 | 2.18 |
	|  3  | 4 | 0.06905 | 0.0 | 2.18 |
	|  4  | 5 | 0.02985 | 0.0 | 2.18 |

	*	add, delete columns:
		*	add columns: there are two ways to add new column: [], .insert(); here we add a rounded INDUS column.<br>
		```
		>>> copy1 = boston_data.copy()
		>>> copy1['round_INDUS'] = round(copy1['INDUS'])
		copy1
		```

		|     | key | feature1 |  ZN | INDUS | round_INDUS |
		| :-: | :-: | :--: | :-: | :---: | :---: |
		|  0  | 1 | 0.02731 | 0.0 | 7.07 | 7.0 |
		|  1  | 2 | 0.02729 | 0.0 | 7.07 | 7.0 |
		|  2  | 3 | 0.03237 | 0.0 | 2.18 | 7.0 |
		|  3  | 4 | 0.06905 | 0.0 | 2.18 | 2.0 |
		|  4  | 5 | 0.02985 | 0.0 | 2.18 | 2.0 |

		```
		>>> copy2 = boston_data.copy()
		>>> copy2.insert(1, 'round_INDUS', round(copy2['INDUS']))
		copy2
		```

		|     | key | round_INDUS| feature1 |  ZN | INDUS |
		| :-: | :-: | :---: | :--: | :-: | :---: |
		|  0  | 1 | 7.0 | 0.02731 | 0.0 | 7.07 |
		|  1  | 2 | 7.0 | 0.02729 | 0.0 | 7.07 |
		|  2  | 3 | 2.0 | 0.03237 | 0.0 | 2.18 |
		|  3  | 4 | 2.0 | 0.06905 | 0.0 | 2.18 |
		|  4  | 5 | 2.0 | 0.02985 | 0.0 | 2.18 |

		*	delete columns: there are three ways to delete columns: del, .pop(), .drop(). del deletes the original form; .pop() deletes the original form and return the deleted column; .drop() returns the new form.<br>
		.drop() default drop row data, do when we want to drop column data: `df.drop(columns=[column_name])`
	*	insert, delete row data:
		*	insert row data: use `df.append(DataFrame, columns=)` and the new row will insert at the last row.<br>
		ex.
		```
		>>> boston_data = boston_data.append(pd.DataFrame([[506,0,0,0]]), columns=boston_data.columns)
		>>> boston_data
		```

		|     | key | CRIM |  ZN | INDUS |
		| :-: | :-: | :--: | :-: | :---: |
		|  0  | 1 | 0.02731 | 0.0 | 7.07 |
		|  1  | 2 | 0.02729 | 0.0 | 7.07 |
		|  2  | 3 | 0.03237 | 0.0 | 2.18 |
		|  3  | 4 | 0.06905 | 0.0 | 2.18 |
		|  4  | 5 | 0.02985 | 0.0 | 2.18 |
		| ... | . | ... | ... | ... |
		| 504 | 505 | 0.4741 | 0.0 | 11.93 |
		| 0 | 506 | 0.0000 | 0.0 | 0.00 |

		*	delete row data: use `df.drop([row_index])`
* * *
*	data filter, selection:
	*	we can use [] or .loc[] to do boolean logical selection. .loc[] can choose columns at the same time, but [] can't.<br>
	ex.
	```
	>>> stock_data = pd.read_csv('STOCK_DAY_0050_202010.csv')
	>>> stock_data[stock_data.open < 104]
	```

	|     | date | open | high | low | close |
	| :-: | :-:  | :-:  | :-:  | :-: | :-:   |
	|  0  | 109/10/05 | 103.45 | 104.05 | 103.0 | 103.05 |
	| 18  | 109/10/30 | 103.55 | 103.60 | 102.7 | 103.00 |

	`stock_data[stock_data.open < 104]` is equivalent to `stock_data.loc[stock_data.open < 104]`

	ex. (.loc[] can choose columns)

	```
	>>> stock_data.loc[(stock_data.open < 104) & (stock_data.close > 103), ['open', 'close']]
	```

	|     | open | close |
	| :-: | :-:  | :---: |
	|  0  | 103.45 | 103.05 |

	*	.iloc[] filters by assigning index:<br>
	```
	>>> stock_data.iloc[3:6]
	```

	|     | date | open | high | low | close |
	| :-: | :-:  | :-:  | :-:  | :-: | :-:   |
	|  3  | 109/10/08 | 105.45 | 106.35 | 105.3 | 106.20 |
	|  4  | 109/10/12 | 106.70 | 107.70 | 106.7 | 107.05 |
	|  5  | 109/10/13 | 107.35 | 107.60 | 106.2 | 107.10 |

	```
	>>> stock_data.iloc[3:6, :2]
	```

	|     | date | open |
	| :-: | :-:  | :-:  |
	|  3  | 109/10/08 | 105.45 |
	|  4  | 109/10/12 | 106.70 |
	|  5  | 109/10/13 | 107.35 |



