class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #start with 0 index
        #search for target - index value
        # if it exists return both indicies 
        # if not move on
        # O(n) - Time complexity
        # O(n)

        seen = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in seen:
                return [seen[diff], index]
            seen[value] = index
        return []







