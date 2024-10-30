# @lcpr-before-debug-begin
from python3problem189 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=189 lang=python3
# @lcpr version=30204
#
# [189] 轮转数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp = []
        # for i in range(-k,0,1):
        #     temp.append(nums[i])
        # for i in range(len(nums)-3):
        #     temp.append(nums[i])
        # nums = temp
        # return nums
        def reverse(i:int, j:int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-1,-100,3,99]\n2\n
# @lcpr case=end

#

