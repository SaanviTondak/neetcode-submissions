class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        n = len(nums)
        output = [1] * n 
        left = 1  #start of w 1 as number on the left

        for i in range(n): #multiply by numbers on the left
            output[i] *= left 
            left *= nums[i] #change the number to the left 
        
        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right 
            right *= nums[i]
        
        return output #multiple rigth and left 