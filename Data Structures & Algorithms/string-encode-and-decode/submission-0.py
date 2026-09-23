class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        res = []

        for string in strs:
            new_string = str(len(string)) + "#" + string
            res.append(new_string)
        
        encoded_str = "".join(res)
           
           
           ## 
          ##.   3#cat2#hi5#hello


        return encoded_str



    def decode(self, s: str) -> List[str]:
        i= 0 
    
        res = []

        while (i < len(s)):

            j = i 
            while s[j] != "#":
                j+=1 
            length = int(s[i:j])

            start = j+1 
            res.append(s[start:start+length])
            i = start+ length
        return res
            

