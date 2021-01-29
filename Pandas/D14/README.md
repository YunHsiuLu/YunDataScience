# D14: Pandas Write Pivot Analysis Form

With some special analysis, we may convert some indexes into columns, or opposite.

* * *
* convert columns into index:
	*	.stack(): it converts the outtest column into index.
	*	.set_index(column): it converts the assign column into index.
	*	.pivot(index=, columns=,): we can use pivot() to convert the form flexibly.
	*	[More details](https://www.geeksforgeeks.org/how-to-convert-dataframe-column-into-an-index-in-python-pandas/)
*	convert index into columns:
	*	.unstack(): it converts the outtest index into column.
	*	.reset_index(level=None): if default, it converts all index into columns. you can set level with a list, and convert the index in list into columns.
	*	[More skills](https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column)

* * *

Some times we want to make columns into value. For this function we use `.melt()`. If you want to stay some columns, then do `.melt(id_vars=column name)`, or the opposite way, `.melt(value_vars=column name)`.

* * *

*	re-construct data form: we can use .pivot() that has metioned above to re-construct data form flexibly.<br>
ex.<br>
df = 

|     | fff | bbb | baa | zzz |
| :-: | :-: | :-: | :-: | :-: |
|  0  | one |  P  |  2  |  h  |
|  1  | one |  Q  |  3  |  i  |
|  2  | one |  R  |  4  |  j  |
|  3  | two |  P  |  5  |  k  |
|  4  | two |  Q  |  6  |  l  |
|  5  | two |  R  |  7  |  m  |

we can do `df.pivot(index='fff', columns='bbb', values=['baa', 'zzz'])`, the form will convert into:<br>

|     |  P  |  Q  |  R  |  P  |  Q  |  R  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| one |  2  |  3  |  4  |  h  |  i  |  j  |
| two |  5  |  6  |  7  |  k  |  l  |  m  |




