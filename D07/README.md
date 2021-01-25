# NumPy Matrix Functions and Linear Algebra
There are several linear algebra functions for matrix mathmetics, you can get more knowledge on wikipedia. We can categorize into four topic: matrix multiplication, matrix operation, special matrix, matrix decomposition.<br>
*	Matrix Multiplication:
	*	dot product: np.dot(M1, M2). When doing dot product, please care for matrix shape!
	*	inner product: np.inner(M1, M2).
	*	outer product: np.outer(M1, M2).
	*	matmul (or @): np.matmul(M1, M2). It is similar as dot, the difference is below:
		*	if M1 and M2 are 2D array, then np.matmul(M1, M2) is equal to np.dot(M1, M2).
		*	multi-dimension array in matmul, take former (n-2) dimension as elements of latter 2 dimension, then do the multiplication.
		*	it's not allow for multiplication between scalar and vector(matrix).
		*	matmul is equivalent to @ sign.
		```
		>>> A = np.arange(6).reshape(2,3)
		>>> B = np.arange(12).reshape(3,4)
		>>> np.matmul(A, B)
		array([[20, 23, 26, 29],
			   [56, 68, 80, 92]])
		>>> A @ B
		array([[20, 23, 26, 29],
			   [56, 68, 80, 92]])
		```
* * *
*	Matrix Operation:
	*	trace: np.trace(M). determination of trace is summation of diagonal of a nxn matrix
	*	determinant: np.linalg.det(M). return the determinant of the matrix M.
	*	inverse: np.linalg.inv(M). return the inverse matrix of the matrix M.
	*	transpose: np.transpose(M). return the transpose matrix of the matrix M.
	*	eigenvalue, eigenvector: np.linalg.eig(M). return eigenvalues and eigenvectors two components. It requires M should be square matrix. we can also use np.linalg.eigvals(A) to get eigenvalues of A, and it doesn't require the matrix format. There are several functions in: [numpy.linalg.eig](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)
	*	rank: np.linalg.matrix_rank(M). return the rank of matrix.
	*	solve: we can solve the linear system by np.linalg.solve(A, b), where A is a coefficient matrix, and b is a dependent variable values. It can return solutions. The equation is `Ax = b`
* * *
*	Spectial Matrix:
	*	Identity: np.identity(c), where c is positive number. It returns diagonal elements are 1 square matrix.
	*	Eye: np.eye(a, b=None, k=0, dtype=float). It can return non-square identity matrix.<br>
	ex.
	```
	>>> np.eye(5, 4, dtype=int)
	array([[1, 0, 0, 0],
		   [0, 1, 0, 0],
		   [0, 0, 1, 0],
		   [0, 0, 0, 1],
		   [0, 0, 0, 0]])
	>>> np.eye(3, k=1)
	array([[0., 1., 0.],
		   [0., 0., 1.],
		   [0., 0., 0.]])
	```
	*	Diagonal Matrix: np.diagonal(M, offset=0). It can return the diagonal vector. The function is same as M.diagonal(offset=0).
	*	Triangle Matrix: np.tri(a, b, offset=0, dtype=float). It can return down-tri-value matrix with a offset.<br>
	ex.
	```
	>>> np.tri(3)
	array([[1., 0., 0.],
		   [1., 1., 0.],
		   [1., 1., 1.]])
	>>> np.tri(3,4)
	array([[1., 0., 0., 0.],
           [1., 1., 0., 0.],
           [1., 1., 1., 0.]])
    >>> np.tri(3,4,1,dtype=1)
    array([[1, 1, 0, 0],
           [1, 1, 1, 0],
           [1, 1, 1, 1]])
	```
	*	Upper triangular, Lower Triangular Matrix: np.triu(M), np.tril(M). As title.
*	Matrix Decomposition:
	*	Cholesky Decomposition: np.linalg.cholesky(M). Requires M is positive definite.<br>
	ex.
	```
	>>> A = np.array([[1, 2], [2, 5]])
	>>> np.linalg.cholesky(A)
	array([[1, 0],
		   [2, 1]])
	```
	*	QR Decomposition: np.linalg.qr(M). Return Q and R matrix.<br>
	[Wikipedia_QR](https://en.wikipedia.org/wiki/QR_decomposition)
	*	SVD Decomposition: np.linalg.svd(M). Return U, S, V* matrix.<br>
	[Wikipedia_SVD](https://en.wikipedia.org/wiki/Singular_value_decomposition)







