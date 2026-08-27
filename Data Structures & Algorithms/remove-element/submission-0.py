class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        k = 0

        while i < length:
            if isinstance(nums[i], (int)):
                if nums[i] == val:
                    nums.pop(i)
                    nums.append('_')
                else:
                    k += 1
                    i += 1
            else:
                i += 1
        
        return k