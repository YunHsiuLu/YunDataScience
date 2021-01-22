# NumPy Access Any Files Content
*	numpy has a self-high-access efficiency file format, .npy file. We can store and load by np.save() and np.load().
*	we can use savetxt() and loadtxt() to read and save txt files.
*	genfromtxt() is a powerful function that it can load array information from txt files.
* * *
*	Numpy I/O: save(), savez(), load():
	*	np.save(): it can store a single array in a ".npy" file.
	*	np.savez(): it can store several arrays in a ".npz" file.
	*	np.load(): return the array(s) in .npy or .npz file.
	*	np.savetxt(): np.savetxt() can save 1D or 2D array in txt file, and set the elements format, delimiter, changeline character, header, footer, etc. Mention that, we should add brackets to generate the correct delimiter if the array is 1D, or the delimiter will be ignored.
	```
	np.savetxt('test.out', [x], delimiter=',')
	```
	*	np.loadtxt(), np.genfromtxt(): np.genfromtxt() has more powerful functions than np.loadtxt(). When read file by np.genfromtxt(), we can use delimiter to get the correct data format.<br>
	ex.
	```
	>>> np.genfromtxt('test.csv', delimiter=',')
	array([[0., 1., 2., 3., 4.],
        [5., 6., 7., 8., 9.]])
	```
	* * *
	delimiter can also receive a integer, means that read in fix length string.<br>
	ex.
	```
	>>> from io import StringIO
	>>> data = u'  1  2  3\n  4  5 67\n890123  4'
	>>> np.genfromtxt(StringIO(data), delimiter=3)
	array([[  1.,   2.,   3.,
		[  4.,   5.,  67.],
	    [890., 123.,   4.])
	```
	* * *
	if autostrip set True, it can automatically delete space when reading file.<br>
	ex.
	```
	>>> data = u'1, 2 , 4\n 4, 5, 6'
	>>> np.genfromtxt(StringIO(data), delimiter=',', atuostrip=True)
	array([[1., 2., 4.],
		[4., 5., 6.]])
	```
	* * *
	same as loadtxt(), they can ignore the comment line, or header/footer when reading files. We can set what header comment line is.<br>
	ex.
	```
	>>> np.genfromtxt('test.out', comment='#')
	```
	if there are two header lines and one footer line, we can set the ignore lines number to read the correct data.<br>
	ex.
	```
	>>> np.genfromtxt('test.out', comments=None, skip_footer=1, skip_header=2)
	```
	* * *
	names index in np.genfromtxt() can figure out whether there is column name in the file. If there's no column name, we can also assign the column name.<br>
	ex.
	```
	>>> np.genfromtxt('test.out', delimiter=',', names=True)
	array([(1., 2., 3.,), (4., 5., 6.), (7., 8., 9.)], dtype=[('a', '<f8'), ('b', '<f8'), ('c', '<f8')])
	>>> data = StringIO("1 2 3\n 4 5 6")
	>>> np.genfromtxt(data, names="a, b, c")
	array([(1., 2., 3.,), (4., 5., 6.)], dtype=[('a', '<f8'), ('b', '<f8'), ('c', '<f8')])
	```
	also, we can choose which column I want to load in with column name or certain column number. But if there are column name, we "can not" use column index to choose which column I want.<br>
	ex.
	```
	>>> a = u"1,2,3,4,5\n6,7,8,9,10"
	>>> np.genfromtxt(StringIO(a), delimiter=",", names="a, b, c", usecols=("a", "c"))
	array([(1., 3.), (6., 8.)], dtype=[('a', '<f8'), ('b', '<f8')]
	>>> a = u"1 2 3 4 5\n6 7 8 9 10"
	>>> np.genfromtxt(StringIO(a), usecols=(1., -1))
	array([[2., 5.],
		[7., 10.]])
	```
	[More details](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)




