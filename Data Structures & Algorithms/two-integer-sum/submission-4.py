class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            hashmap[n] = i
        
        for i, n in enumerate(nums):
            compliment = target - n

            if compliment in hashmap and i != hashmap[compliment]:
                return [i, hashmap[compliment]]