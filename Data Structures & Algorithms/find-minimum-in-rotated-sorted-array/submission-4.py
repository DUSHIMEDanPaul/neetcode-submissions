class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            
            # If middle is greater than right, min is in the right half
            if nums[m] > nums[r]:
                l = m + 1
            # If middle is less than or equal to right, min is at m or to the left
            else:
                r = m
                
        return nums[l] # l and r will converge on the minimum
