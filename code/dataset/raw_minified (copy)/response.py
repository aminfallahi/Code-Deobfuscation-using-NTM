def A(obj):
	'\n    Checks whether a given file-like object is closed.\n\n    :param obj:\n        The file-like object to check.\n    ';A=obj
	if hasattr(A,'fp'):return A.fp is None
	return A.closed