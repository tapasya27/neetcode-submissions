class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if len 1, return len
        #dict index would be word, 
        #index would be anagram, value would be word
        counts = {}
        for value in strs:
            key = tuple(sorted(value))

            if key in counts:
                counts[key].append(value)
            else:
                counts[key] = [value]

        return list(counts.values())

        