class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        frequency = [[] for _ in range(len(nums) + 1)]
        result = []
        
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for number, count in counter.items():
            frequency[count].append(number)
        
        for i in range(len(frequency) - 1, 0, -1):
            while frequency[i]:
                if len(result) == k:
                    return result
                result.append(frequency[i].pop())
        return result