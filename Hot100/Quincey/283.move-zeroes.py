#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30204
#
# [283] 移动零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 我的解法
        # left = 0
        # n_zero = 0
        # right = len(nums)
        # while left < right:
        #     if nums[left] == 0:
        #         while left+n_zero<right and nums[left+n_zero] == 0:
        #             n_zero += 1
        #         for i in range(left+n_zero,right):
        #             nums[i-n_zero] = nums[i]
        #         nums[right-n_zero:] = [0]*len(nums[right-n_zero:])
        #         right -= n_zero
        #         n_zero = 0
        #     else:
        #         left += 1
        left,right = 0,0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right+=1
            else:
                right+=1                
# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

