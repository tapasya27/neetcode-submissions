from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for word in strs:
            # Use sorted characters as the key
            key = tuple(sorted(word))  # e.g., 'act' -> ('a', 'c', 't')
            grouped[key].append(word)

        return list(grouped.values())
