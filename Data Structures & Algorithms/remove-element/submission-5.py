class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        met = 0

        while val in nums:
            nums.remove(val)
            nums.append(-1)
            met += 1
        
        return len(nums) - met
        

            