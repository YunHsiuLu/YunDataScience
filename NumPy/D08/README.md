# Numpy Structured Arrays
*	numpy data type and corresponding:

Data type | character | Python data type | Numpy uni-dtype 
:-------: | :-------: | :--------------: | :--------------:
boolean | ? | bool | np.bool_
signed byte | b | bytes | np.bytes_
unsigned byte | B | bytes | np.bytes_
signed integer | i | int | np.int_
unsigned int | u | int | np.uint
floating-point | f | float | np.float_
complex-floating point | c | complex | np.cfloat
timedelta | m | datetime.timedelta | np.timedelta64
datetime | M | datetime.datetime | np.datetime64
string | S, a | str | np.str_
Unicode string | U | str | np.str_

we can use `numpy.dtype(s)` to define the data type of input objects. we can also use  dictionary with dtype in advanced way:<br>
ex.
```
>>> dt = np.dtype({'names':('Name', 'num1', 'num2', 'True'),
                   'formats':((np.str_, 5), np.int32, int, 'U3')})
>>> b = np.genfromtxt('structured.txt', delimiter=',', dtype=dt)
>>> b
array([('Jay', 1, 2, 'Yes'), ('James', 3, 4, 'No'), ('Joe', 5, 6, 'Yes')],
      dtype=[('Name', '<U5'), ('num1', '<i4'), ('num2', '<i8'), ('True', '<U3')])
>>> b[0]
('Jay', 1, 2, 'Yes')
>>> b['Name']
array(['Jay', 'James', 'Joe'], dtype='<U5')
>>> b[1]['True']
'No'
>>> b[b['num2'] >= 3]['Name']
array(['James', 'Joe'], dtype='<U5')
```
np.zeros(a, dtype=float) can initialize the array, and set the elements dtype.<br>
```
>>> c = np.zeros(3, dtype=dt)
>>> c
array([('', 0, 0, ''), ('', 0, 0, ''), ('', 0, 0, '')],
      dtype=[('Name', '<U5'), ('num1', '<i4'), ('num2', '<i8'), ('True', '<U3')])
>>> name = ['Chloe', 'Charlotte', 'Clara']
>>> num_1 = [11, 12, 13]
>>> num_2 = [14, 15, 16]
>>> check = ['Y', 'Y', 'N']
>>> c['Name'] = name
>>> c['num1'] = num_1
>>> c['num2'] = num_2
>>> c['True'] = check
>>> print(c)
[('Chloe', 11, 14, 'Y'), ('Charl', 12, 15, 'Y'), ('Clara', 13, 16, 'N')]
```
then we can input the data to the array.
*	Record Array: it supports more attributes to store the structured array, but the efficiency is worse than original array.<br>
```
>>> c_rec = c.view(np.recarray)
>>> c_rec
rec.array([('Chloe', 11, 14, 'Y'), ('Charl', 12, 15, 'Y'), ('Clara', 13, 16, 'N')],
          dtype=[('Name', '<U5'), ('num1', '<i4'), ('num2', '<i8'), ('True', '<U3')])
>>> c_rec.Name
array(['Chloe', 'Charl', 'Clara'], dtype='<U5')
```







