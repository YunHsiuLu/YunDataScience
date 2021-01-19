# NumPy Array Calculation and Mathmetics
*	numpy provide many mathmetical and statistical functions, they can do calculation on an array and return an result array.
*	NumPy calculation: (+, -, *, /)
```
a + b    np.add(a, b)          addition
a - b    np.substract(a, b)    substract
a * b    np.multiply(a, b)     multiply
a / b    np.divide(a, b)       division
a % b    np.mod(a, b)          module
```
*	np.sum(array, axis=None): it will summation all elements in array if axis is None; it will summation all elements in array along with axis if axis has value.
```
>>> np.sum([0.5, 1.5])
2.0
>>> np.sum([[0, 1], [0, 5]])
6
>>> np.sum([[0, 1], [0, 5]], axis = 0)
array([0, 6])
>>> np.sum([[0, 1], [0, 5]], axis = 1)
array([1, 5])
```
*	np.power(base, exponent)
*	np.sqrt(a): do square root. "a" can be a value or a array.
```
>>> a = 4
>>> np.sqrt(a)
2
>>> b = np.array([1, 2, 3, 4])
>>> np.sqrt(b)
array([1., 1.41421356, 1.73205081, 2.])
```
*	np.e, np.exp(): Euler's number and exponential function.
```
>>> np.e
2.718281828459045
>>> np.exp(1)
2.718281828459045
>>> np.exp(np.arange(5))
array([1., 2.71828183, 7.3890561, 20.08553692, 54.59815003])
```
*	logarithm function:
	*	np.log(x): base is e
	*	np.log2(x): base is 2
	*	np.log10(x): base is 10
	*	np.log1p(x): base is e, return log(1+x)
when change to other base number, you can do: (take base is 3 for example)
```
np.log(9)/np.log(3)
```
when log(negative), it will return "NaN", means "not a number".
*	approximation:
	*	round(a, decimals=0), around(a, decimals=0): not normal rounding, for example:
	```
	>>> np.round(2.4)
	2.0
	>>> np.round(2.5)
	2.0
	>>> np.round(2.6)
	3.0
	>>> np.round(251.374, 1)
	251.4
	>>> np.round(251.374, -1)
	250.0
	>>> np.round(251.374, -2)
	300.0
	```
	*	rint(): round to nearest integer.
	```
	>>> np.rint(2.4)
	2.0
	>>> np.rint(2.5)
	2.0
	>>> np.rint(2.6)
	3.0
	>>> np.rint(2.51)
	3.0
	```
	*	trunc(): chop off
	*	floor(), ceil(): chop off, carry up
	*	fix(): take integer in 0 direction
*	absoluted value: np.abs(), np.absolute(), np.fabs().
	*	np.abs() is same as np.absolute(); np.fabs() can't deal with complex number.
	*	np.fabs(complex) returns NaN
*	dot product: np.dot()
	*	inner product


