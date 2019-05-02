class A:
	def canPermutePalindrome(A,s):'\n        :type s: str\n        :rtype: bool\n        ';return sum((A%2 for A in collections.Counter(s).values()))<2