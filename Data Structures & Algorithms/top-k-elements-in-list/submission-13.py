class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.Counter(nums)
        frequencies = [[] for i in range(len(nums) + 1)]

        for key,value in hashmap.items():
            frequencies[value].append(key)
        
        res = []

        for i in range(len(frequencies) - 1, -1, -1):
            for ele in frequencies[i]:
                if len(res) < k:
                    res.append(ele)
                if len(res) == k:
                    break
        return res