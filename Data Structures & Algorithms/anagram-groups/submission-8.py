class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            if tuple(sorted(word)) in groups:
                groups[tuple(sorted(word))].append(word)
            else:
                groups[tuple(sorted(word))] = [word]
        
        return [value for value in groups.values()]