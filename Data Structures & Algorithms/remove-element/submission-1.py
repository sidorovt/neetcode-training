class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        eq = 0

        while val in nums:
            nums.remove(val)
            nums.append(-1)
            eq += 1
        
        return len(nums) - eq