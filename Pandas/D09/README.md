# D09: Using Pandas Read & Write Common Format
*	read & write csv files:
	*	pd.read_csv(filename): returns a table of the csv file; it is equivalent to csv.reader(filename), but csv.reader() returns many arrays.<br>
	```
	>>> iris_data = pd.read_csv('iris.csv')
	>>> iris_data
	```

	|  | sepal length | sepal width | petal length | petal width | target |
	| :---: | :----------: | :---------: | :----------: | :---------: | :----: |
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

	|  | petal length | petal width | target |
	| :-: | :----------: | :---------: | :----: |
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
	| :-: | :-: | :-: | :-: | :-: | :-: |
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
	*	.to_sql(): here shows how to write data base in SQL:<br>
	```
	>>> import sqlite3
	>>> boston_data = pd.read_excel('data.xls', sheet_name='boston',
									header=0, usecols=['TAX', 'PTRATIO', 'B', 'LSTAT'])
	>>> connection = sqlite3.connect('sql_db.sqlite')
	>>> boston_data.to_sql('boston', connection, if_exists='replace')
	>>> connection.commit()
	>>> connection.close()
	```
	the example shows that it reads sheet 'boston' in excel file 'data.xls' first, then connect to sqlite3 database. if_exist will check if there exists the data base named 'boston'.
	*	pd.io.sql.read_sql(): this is how to read from SQLite3 data base.
	here are two link for SQLite3 read & write:
	[.to_sql](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html)
	[read_sql()](https://sodocumentation.net/zh-tw/pandas/topic/2176/將sql-server讀取到dataframe)





