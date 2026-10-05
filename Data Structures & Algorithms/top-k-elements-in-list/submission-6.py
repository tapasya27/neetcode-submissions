class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return empty list if empty
        # Create a hashmap which counts the frequencies of all recurring nums
        # if the values are greater than equal to values return the list 

        if len(nums) == 0:
            return []

        result = []
        counts = {}

        for index, value in enumerate(nums):
            if value in counts:
                counts[value] +=1
            else:
                counts[value] = 1

        
        result = list(dict(sorted(counts.items(), key=lambda item: item[1])))[-k:]
        return result