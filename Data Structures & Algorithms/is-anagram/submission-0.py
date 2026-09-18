class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #constraint-> number of times, cannot use hashmap/dict mtd 
        #dict with counter as value 
        #two dicts with counter and compare frequencies 

        s_dict = {} #key as letter, value as frequency 
        t_dict = {}

        for i in s: #o(n)
            if i in s_dict:
                s_dict[i] += 1 #increase frequency counter 
            else:
                s_dict[i] = 1 

        for n in t: #o(n)
            if n in t_dict:
                t_dict[n] += 1
            else:    
                t_dict[n] = 1      


        if s_dict == t_dict:
            return True 
        return False 

