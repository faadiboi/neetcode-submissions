class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 1
        left = [1]*len(nums)
        while i<len(nums):
            left[i] = left[i-1]*nums[i-1]
            i+=1
        
        i = len(nums)-1
        right = [1]*len(nums)
        while i>0:
            right[i-1]=right[i]*nums[i]
            i-=1
        
        j = 0
        output = [1]*len(nums)
        while j<len(nums):
            output[j]=left[j]*right[j]
            j+=1
        return output
