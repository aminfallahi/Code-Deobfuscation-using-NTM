class A:
	def wiggleSort(C,nums):
		'\n        :type nums: List[int]\n        :rtype: void Do not return anything, modify nums in-place instead.\n        ';B=nums
		for A in xrange(1,len(B)):
			if A%2 and B[A-1]>B[A]or not A%2 and B[A-1]<B[A]:B[A-1],B[A]=B[A],B[A-1]