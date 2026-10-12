class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            res[tuple(sorted(string))].append(string)
        
        output = []

        for r in res.values():
            output.append(r)

        return output