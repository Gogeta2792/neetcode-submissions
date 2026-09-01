class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_words = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in seen_words:
                seen_words[key].append(word)
            else:
                seen_words[key] = [word]
            
        return [value for value in seen_words.values()]