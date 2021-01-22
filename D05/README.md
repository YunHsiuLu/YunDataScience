# NumPy Statistics Functions
*	Order Statistics
	*	np.maximum(), np.minimum(): element-wise compare two arrays and return the maximum or minimum; if the compared element is NaN, return nan.
	*	np.fmax(), np.fmin(): similar to above, the difference is if the compared element is NaN, return the non-nan element.
	*	np.nanmax(), np.nanmin(): return the maximum or minimum in an nan-exist array.
	*	np.percentile(), np.nanpercentile(): calculate the percent value in an array; the latter one will ignore the NaN value.<br>
	ex.
	```
	>>> a = np.array([1,2,3,4,5])
	>>> np.percentile(a, 50)
	3.0
	>>> np.percentile(a, 25)
	2.0
	>>> np.percentile(a, 10)
	1.2
	```
	it can also assign an axis.<br>
	ex.
	```
	>>> a = np.array([[1,2,3], [4,5,6]])
	>>> np.percentile(a, 50, axis=0)
	array([2.5, 3.5, 4.5])
	>>> np.percentile(a, 50, axis=1)
	array([2.0, 5.0])
	```
	*	np.quantile(), np.nanquantile(): equivalent to percentile(), but value range is [0, 1]; np.quantile(..., 0.5) is equivalent to np.percentile(..., 50)
*	Mean Values and Variance
	*	np.mean(), np.nanmean(): calculate the mean value of an array, return nan if there is nan in the array. The latter one will ignore the nan value and calculate the mean value.
	*	np.average(): it can calculate the weight-meanvalue. On the other hand, avg = sum(a * weights)/sum(weights)<br>
	ex.
	```
	>>> a = np.array([1,2,3,4,5])
	>>> np.average(a, weights=[4,3,2,1,0])
	2.0
	```
	the calculation above is: (1*4+2*3+3*2+4*1+5*0)/(4+3+2+1+0) = 2.0
	*	np.median(), np.nanmedian(): calculate the median value of an array, return nan if there's nan in the array. Same as above, np.nanmedian will ignore nan value.
	*	np.std(), np.nanstd(): calculate the standard deviation of an array, return nan if there's nan in the array.  Same as above.
	*	np.var(), np.nanvar(): calculate the variance of an array, return nan if there's nan in the array. Same as above.
*	Correlation
	Links below can give more details of mathmetics.
	*	np.corrcoef(): [More corrcoef details!!!](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)
	*	np.corrlate(): [More corrcoef details!!!](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)
	*	np.cov(): [More corrcoef details!!!](https://numpy.org/doc/stable/reference/generated/numpy.cov.html)
*	Histogram
	*	Using arrays to represent the histogram informations. np.histogram() returns histogram value and bin edge.
	```
	>>> a = np.array([0,0,1,0,1,1,0,1,0,0,1,0,0,0,0,1,1,1])
	>>> np.histogram(a, bins=[-0.5, 0.5, 1.5])
	array([10, 8]), array([-0.5, 0.5, 1.5])
	```
	it will look like:
	![plot](Figure1.png)
