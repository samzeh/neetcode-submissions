class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i, str in enumerate(strs):
            if sorted(strs) not in groups:
                groups[sorted(strs)] = str
        
        return list(groups.values())


        
        