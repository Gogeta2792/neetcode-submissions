class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]
        frequencies = {}

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        for key, value in frequencies.items():
            count[value].append(key)

        results = []

        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                results.append(n)
                if len(results) == k:
                    return results