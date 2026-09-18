class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplist = set() #initialise set 

        for num in nums: #o(n) iteration
            if num in duplist: #o(1) lookup
                return True 
            duplist.add(num) #o(1) insertion
        return False 