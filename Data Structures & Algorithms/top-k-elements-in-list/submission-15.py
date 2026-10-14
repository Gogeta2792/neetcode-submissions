class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            bucket[value].append(key)
        
        res = []

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                if len(res) < k:
                    res.append(num)
                else:
                    return res
        
        return res