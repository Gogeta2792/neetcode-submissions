class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        frequencies = [[] for _ in range(len(nums) + 1)]

        for num, count in hashmap.items():
            frequencies[count].append(num)
        
        res = []

        #iterate backwards through frequencies
        for i in range(len(frequencies) - 1, -1, -1):
            for j in frequencies[i]:
                if len(res) < k:
                    res.append(j)
        
        return res