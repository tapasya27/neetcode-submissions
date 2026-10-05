class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #start with 0 index
        #search for target - index value
        # if it exists return both indicies 
        # if not move on
        # O(n) - Time complexity
        # O(n)

        #if len(nums) == 2:
            #return [0,1]

        #for index, value in enumerate(nums):
            #diff = target - value
            #if diff in nums:
                #return [index, nums.index(diff)]
        seen={}
        for i in range(len(nums)):
            complement= target-nums[i]
            if complement in seen:
                return ([seen[complement],i])
            seen[nums[i]]=i









