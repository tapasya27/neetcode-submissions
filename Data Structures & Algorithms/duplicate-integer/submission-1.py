class Solution: 
	def hasDuplicate(self, nums: List[int]) -> bool:
		#Edge case 1: empty array
		if len(nums) == 0:
			print("empty array")
			return False
		# Sorted array
		nums.sort()
		#For loop to check if the next number is same as the prev number
		for i in range(len(nums)-1):
			if nums[i] == nums[i+1]:
				return True
		return False
