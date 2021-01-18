# Python Data Science

**D01: NumPy Basic Exercise**

install and import NumPy

*	you can use `pip install numpy` or `pip3 install numpy`; execute `conda install numpy` in Anaconda base

*	import numpy:

`import numpy as np`

*	check the numpy version:

`np.__version__`

be careful that there are double '_' prefix and post of version
* * *
if you don't want to download anaconda and do have python3:

`python3 -m pip install jupyter`

for installing jupyter notebook in local

then you can open jupyter notebook with webviewer at folder:

`jupyter notebook [folder]`

* * *

**D02: Advanced Array Exercise**

*	array reshape:
	*	flatten(), ravel(): multi-dimension to 1-D, but ravel() is based on original array.
	*	reshape(): reshape array A1 into another array A2, request that number of elements in A1 equals to number of elements in A2.
	```
	     [ 1 2 ]                                   [ 1 2 3]
	A1 = [ 3 4 ], reshape A1 into 2*3 matrix, A2 = 
	     [ 5 6 ]                                   [ 4 5 6]
	```
	*	resize(): reshape array A1 into another array A2, if the number of elements in A1 differs to number of element in A2, insert 0 at the end.
*	axis and dimension
*	array merging and array splitting
*	array iteration
*	array searching and sorting