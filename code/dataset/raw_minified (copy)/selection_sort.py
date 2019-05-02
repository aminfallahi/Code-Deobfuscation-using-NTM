D=len
C=range
def A(a):
	"\n    Sorts the list 'a' using Selection sort algorithm\n\n    >>> from pydsa import selection_sort\n    >>> a = [3, 4, 2, 1, 12, 9]\n    >>> selection_sort(a)\n    [1, 2, 3, 4, 9, 12]\n\n    "
	for A in C(D(a)):
		for B in C(A,D(a)):
			if a[B]<a[A]:a[A],a[B]=a[B],a[A]
	return a