# D09: Using Pandas Read & Write Common Format
*	read & write csv files:
	*	pd.read_csv(filename): returns a table of the csv file; it is equivalent to csv.reader(filename), but csv.reader() returns many arrays.<br>
	```
	>>> iris_data = pd.read_csv('iris.csv')
	>>> iris_data
	```


	| index | sepal length | sepal width | petal length | petal width | target |
	| *---* | *----------* | *---------* | *----------* | *---------* | *----* |
	| 0 | 5.1 | 3.5 | 1.4 | 0.2 | 0 |
	| 1 | 4.9 | 3.0 | 1.4 | 0.2 | 0 |
	| 2 | 4.7 | 3.2 | 1.3 | 0.2 | 0 |
	| 3 | 4.6 | 3.1 | 1.5 | 0.2 | 0 |
	| 4 | 5.0 | 3.6 | 1.4 | 0.2 | 0 |

	we can assign the columns for reading:<br>
	```
	>>> iris_data = pd.read_csv('iris.csv', usecols=['petal length', 'petal width', 'target'])
	>>> iris_data
	```

	| index | petal length | petal width | target |
	| *-* | *----------* | *---------* | *----* |
	| 0 | 1.4 | 0.2 | 0 |
	| 1 | 1.4 | 0.2 | 0 |
	| 2 | 1.3 | 0.2 | 0 |
	| 3 | 1.5 | 0.2 | 0 |
	| 4 | 1.4 | 0.2 | 0 |

	also we can edit the header name:<br>
	```
	>>> iris_data = pd.read_csv('iris.csv', header=0, names=['f1', 'f2', 'f3', 'f4', 'target'])
	>>> iris_data
	```

	|     | f1 | f2 | f3 | f4 | target |
	| *-* | *-* | *-* | *-* | *-* | *-* |
	| 0 | 5.1 | 3.5 | 1.4 | 0.2 | 0 |
	| 1 | 4.9 | 3.0 | 1.4 | 0.2 | 0 |
	| 2 | 4.7 | 3.2 | 1.3 | 0.2 | 0 |
	| 3 | 4.6 | 3.1 | 1.5 | 0.2 | 0 |
	| 4 | 5.0 | 3.6 | 1.4 | 0.2 | 0 |

	*	df.to_csv(): we should set df to pd.DataFrame(), here is example:<br>
	```
	>>> cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }
    >>> df = pd.DataFrame(cars, columns= ['Brand', 'Price'])
    >>> df.to_csv(path, index=False, header=True)
	```

*	read & write excel files:
	*	pd.read_excel(): it supports Excel 2003 later format data; it uses XLRD or OpenPyXL library, make sure that you have installed one of them.<br>
	it default reads the first work sheet in excel, we can use sheet_name option to read other work sheet.
	*	.to_excel(): the output way is same as .to_csv().

*	read & write json files:
	*	pd.read_json()
	*	.to_json()

*	read & write SQL data base:
	





