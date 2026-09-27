class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums) 
        
        max_length = 0 
        start_of_seq = 0

        for n in nums: 
            if (n-1) not in seq:
                current_number = n 
                current_length = 1 

                while (current_number + 1 ) in seq:
                    current_length += 1 
                    current_number +=1 
                
                max_length = max(max_length, current_length)
        
        return max_length



        