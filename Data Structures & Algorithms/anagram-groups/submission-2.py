class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for word in strs:
            if tuple(sorted(word)) in words:
                words[tuple(sorted(word))].append(word)
            else:
                words[tuple(sorted(word))] = [word]
        
        output = []

        for value in words.values():
            output.append(value)

        return output