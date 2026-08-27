class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        while val in nums:
            nums.remove(val)
            nums.append(-1)
            ans += 1
        return len(nums) - ans