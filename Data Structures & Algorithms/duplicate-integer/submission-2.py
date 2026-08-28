class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        
        for key, value in hashmap.items():
            if value > 1:
                return True
        
        return False

        

            