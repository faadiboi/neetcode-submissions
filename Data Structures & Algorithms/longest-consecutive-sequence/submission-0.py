class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0 
        numbers = set(nums)
        for x in numbers:
            if x-1 not in numbers:
                largest = 1
                while x+1 in numbers:
                    largest+=1
                    x+=1
                if largest>longest:
                    longest = largest
        return longest