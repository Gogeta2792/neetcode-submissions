class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num, index in count.items():
            frequency[index].append(num)
            
        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for number in frequency[i]:
                if len(result) == k:
                    return result
                else:
                    result.append(number)

        return result

# Naive
# Have a hashmap
# key is num, value is count of num
# return top k counts.
# Dictionary not iterable in that way
# Can't easily retrieve top k
# Hence, change Data Structure

# Array has index and value
# What if index was the count of numbers, value is a list of the numbers that have that count
# Hence, automatically, it will be sorted by least to most frequent
# We can iterate from the last element in the array