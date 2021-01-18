# D02: Advanced Array Exercise
*	array reshape:
	*	flatten(), ravel(): multi-dimension to 1-D.<br>
	ex.
	```
	>>> a1 = np.array([[1,2,3],[4,5,6]])
	>>> a_flatten = a1.flatten()
	>>> a_flatten
	array([1,2,3,4,5,6])
	>>> a_ravel = a1.ravel()
	>>> a_ravel
	array([1,2,3,4,5,6])
	```
	*	reshape(): reshape array A1 into another array A2, request that number of elements in A1 equals to number of elements in A2. order='F' means reshape by row; order='C' means reshape by column.<br>
	ex.
	```
	     [ 1 2 ]
	A1 = [ 3 4 ], reshape A1 into 2*3 matrix
	     [ 5 6 ]
	>>> A1 = np.array([[1, 2], [3, 4], [5, 6]])
	>>> A1.reshape((2,3))
	array([[1, 2, 3],
           [4, 5, 6]])
    ```
    reshape A1 by row or by column.
    ```
    >>> A1.reshape((2,3), order='F')
    array([[1,5,4],
           [3,2,6]])
    >>> A1.reshape((2,3), order='C')
    array([1,2,3[],
           [4,5,6]])
	```
	*	resize(): reshape array A1 into another array A2, if the number of elements in A1 differs to number of element in A2, insert 0 at the end.<br>
	ex. 
	```
	     [ 1 2 ]                                   [ 1 2 ]
	A1 = [ 3 4 ], resize A1 into 2*4 matrix, A2 =  [ 3 4 ]
	     [ 5 6 ]                                   [ 5 6 ]
	                                               [ 1 2 ]
	```

	```
	>>> A1 = np.array([[1, 2], [3, 4], [5, 6]])
	>>> A2 = np.resize(A1, (2,4))
	>>> A2
	array([[1, 2],
		   [3, 4],
		   [5, 6],
		   [1, 2]])
	```
*	axis and dimension:
	```
	1D:            2D:               3D:
	  axis 0              1                         2
	--------->      | -------->                ----------->
	[ 1,2,3 ]       | [[ 1,2,3 ],     | 1 | [[[ 111,112,113 ],
	              0 |  [ 4,5,6 ],     |   v   [ 121,122,123 ]],
	                v  [ 7,8,9 ]]     |      [[ 211,212,213 ],
	                                0 |       [ 221,222,223 ]],
	                                  |      [[ 311,312,313 ],
	                                  v       [ 321,322,323 ]]]
	```
*	array merging and array splitting:
	*	Merge:
		*	concatenate(): merge assigned axis (default: axis 0), request that shape should be same except for assigned axis.<br>
		ex.
		```
		>>> A1 = np.array([[1, 2], [3, 4]])
		>>> A2 = np.array([[5, 6]])
		>>> np.concatenate((A1, A2), axis = 0)
		array([[1, 2],
			   [3 ,4],
			   [5, 6]])
		>>> np.concatenate((A1, A2.T), axis=1)
		array([[1, 2, 5],
       	       [3, 4, 6]])
		>>> np.concatenate((A1, A2), axis=None)
		array([1, 2, 3, 4, 5, 6])
		```
		*	stack(), hstack(), vstack(): stack() will return the array but dimension plus 1; hstack and vstack are horizontal stack and vertical stack.<br>
		ex.
		```
		>>> A1 = np.array([1,2,3])
		>>> A2 = np.array([4,5,6])
		>>> np.stack((A1, A2), axis=0)
		array([[1,2,3],
			   [4,5,6]])
		>>> np.stack((A1, A2), axis=1)
		array([[1,2],
			   [3,4],
			   [5,6]])
		>>> np.hstack((A1, A2))
		array([1,2,3,4,5,6])
		>> np.vstack((A1, A2))
		array([[1,2,3],
			   [4,5,6]])
		```
	*	Split:
		* split(), hsplit(), vsplit(): split() can split certain elements at assigned axis; hsplit() and vsplit() are horizontal split and vertical split. All of them will return the split result in a list, and the dimension won't be change.<br>
		ex.
		```
		>>> A3 = np.array([[1,2,3], [4,5,6]])
		>>> np.split(A3, 2, axis = 0)
		[array([[1,2,3]]),
		 array([[4,5,6]])]
		>>> np.split(A3, 3, axis = 1)
		[array([[1], [4]]),
		 array([[2], [5]]),
		 array([[3], [6]])]
		>>> np.hsplit(A3, 3)
		[array([[1], [4]]),
		 array([[2], [5]]),
		 array([[3], [6]])]
		>>> np.vsplit(A3, 2)
		[array([[1,2,3]]),
		 array([[4,5,6]])]
		```
*	array iteration:
*	array searching and sorting:
	*	amax(), amin(), max(), min(): amax() and max() are same function but in different library, amin() and min() respectively.<br>
	ex.
	```
	        numpy object                         ndarray object
	np.amax(array, axis=None, keepdims=)  ndarray.max(axis=None, keepdims)
	np.amin(array, axis=None, keepdims=)  ndarray.min(axis=None, keepdims)
	```
	*	argmax(), argmin(): they do return the index which is max or min in array.<br>
	ex.
	```
	      numpy object                ndarray object
	np.argmax(array, axis=None)  ndarray.argmax(axis=None)
	np.argmin(array, axis=None)  ndarray.argmin(axis=None)
	```
	*	where(condition): return the **index** that is agreed with the condition.<br>
	```
	>>> A1 = np.arange(10)
	>>> A1
	array([0,1,2,3,4,5,6,7,8,9])
	>>> np.where(A1 < 5)
	array([0,1,2,3,4])
	```
	*	where(condition, x, y): return the elements that is agreed with the condition. x is the value if condtion is true; y is opposite.<br>
	ex.
	```
	>>> np.where(A1 < 5, A1, A1*10)
	array([0,1,2,3,4,50,60,70,80,90])
	```
	*	nonzero(): equals to np.where(array != 0)<br>
	ex.
	```
	>>> A1 = np.array([0,1,0,0,1,0,1,0])
	>>> np.nonzero(A1)
	array([1,4,6])
	```
	*	sort(array, axis=-1, kind=None), argsort(array, axis=-1, kind=None): return the sorted list or index of sorted list, from small to large elements.<br>
	ex.
	```
	>>> A1 = np.array([[1,4],[3,1]])
	>>> np.sort(A1)
	array([[1,4],
	       [1,3]])
	>>> np.sort(A1, axis=None)
	array([1,1,3,4])
	>>> np.sort(A1, axis=0)
	array([[1,1],
	       [3,4]])
	>>> np.argsort(A1)
	array([[0,1],[1,0]])
	```
	Also, we can choose the different sorted algorithm, there are quick sort (default), merge sort, timesort, heapsort, etc. By the algorithm timing count, the quick sort is the quickest sorting algorithm. We can change the algorithm at kind.<br>
	ex.
	```
	>>> np.sort(A1, axis=-1, kind='quicksort')
	array([[1,4],
	       [1,3]])
	```




