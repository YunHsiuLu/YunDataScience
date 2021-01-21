# D04: NumPy Array Logic Functions
*	Array contents:
	*	isnan(): return True if the element is NaN; otherwise False.
	*	isfinite(): return True if the element is finite; otherwise False.
	*	isinf(), isposinf(), isneginf(): return True if element is infinite, positive infinite, negative infinite respectively; otherwise False.
	*	isnat(): return True if the element is "not" a time; otherwise False.
*	Array type testing:
	*	isscalar(): return True if the element is a scalar; otherwise False.
	*	isreal(): return True if the element is a real "number"; otherwise False.
	*	iscomplex(): return True if the element is a complex "number"; otherwise False.
	*	isrealobj(): return True if the element is a real "object"; otherwise False.
	*	iscomplexobj(): return True if the element is a complex "object"; otherwise False.
*	Comparison:
	*	array_equal(): compare two lists whether have same shape and same elements. If yes, reture True; otherwise False.
	*	array_equiv(): same as above, but it can compare two different dimension list.
	ex.
	```
	>>> a = [1,2,3,4]
	>>> b = [1,2,3]
	>>> np.array_equal(a,b)
	False
	>>> c = [[1,2,3], [1,2,3]]
	>>> np.array_equal(b,c)
	False
	>>> np.array_equiv(b,c)
	True
	```
*	Logic operations: logical_and(), logical_or(), logical_not(), logical_xor().
	*	They can only compare "two" list of boolean value.
*	Truth value testing:
	*	all(): check whether there is "not" 0 or "False" in an array, if yes, return True; otherwise False.
	*	any(): check whether there is "any" value or "True" in an array, if yes, return True; otherwise False.


