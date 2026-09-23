class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap -> for loop -> if num not in hashmap +1 -> 
        count = {} 

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1 
        
        #frequency map created {1:3, 2:7, 4:20}
        buckets = [[] for _ in range(len(nums) +1 )] #buckets start from 0 to len(nums)


        for num, freq in count.items() :
            buckets[freq].append(num)
        
        result = []

        for i in range(len(buckets) -1, -1, -1):
            result.extend(buckets[i])
            if len(result) >k:
                return result[:k]
        return result 