class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		#Quick check via length
		if len(s) != len(t):
			return False
		dict1 = {}
		dict2 = {}
		#one pointers checking from front and back for both words
		for i in range(len(s)):
			if s[i] not in dict1:
				dict1[s[i]] = 0
			else:
				dict1[s[i]] += 1
		for i in range(len(t)):
			if t[i] not in dict2:
				dict2[t[i]] = 0
			else:
				dict2[t[i]] += 1

		if dict1 == dict2:
			return True
		else:
			return False