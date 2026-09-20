class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            freq = [0] * 26 #[0,0,0....,0]

            for letter in string:
                freq[ord(letter) - ord("a")] += 1 #ord func gives ascii value of letter
            hashmap[tuple(freq)].append(string) #key in hashmap must be immutable hence tuple not list 
        return list(hashmap.values())


        #o(m * n) where m is no of strings and n is avg lentgh of strings 

        