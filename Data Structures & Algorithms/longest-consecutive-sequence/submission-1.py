class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest_Consecutive = 0

        for num in nums:
            if num - 1 not in numbers:
                #This is the first element in its array.
                #Find out how long the array is
                tmp = num
                curr_longest = 0
                while tmp in numbers:
                    tmp += 1
                    curr_longest += 1
                longest_Consecutive = max(curr_longest, longest_Consecutive)

        return longest_Consecutive

# Naive solution
# Sort the list, iterate though the list once while keeping track of if the string is still consecutive.
# Once the string is no longer consecutive, compare the length with the longest length so far. Keep track of the longest length.
# Once we have iterated through the list, then we return longest length
# However, this does not work because sorting the list would require O(log n), and iterating through the list again is another O(n) and that is against the question's boundaries as it would add up to O(n log n)

# Hence, we know that sorting is not viable.
# Because of this, I have the idea that we must iterate through the nums list exactly one time while keeping track of certain things.
# When trying to ideate what those things could be, I believe that it could be useful to take in the number and figure out both one minus and one plus that number.
# Then, when iterating to another number, we add it to the previous number's list if and only if it is in either the one minus or one plus position
# Otherwise, we would create a new list for that number with its minus and plus one as well
# I see as well that there could be an issue with this. If the initial array is nums = [2,20,4,10,3,4,5]
# Then we have [1,2,3] ,add 20, then when we add 4 we have [3,4,5] and then when we add 3 afterwards we would somehow have to link the two lists to become [1,2,3,4,5]
# My idea was to keep track of all the numbers in the list alongside the plus one and minus one of the largest and smallest numbers respectively, but I am not sure how I would end up linking the lists if a scenario like the one I mentioned prior were to occur.