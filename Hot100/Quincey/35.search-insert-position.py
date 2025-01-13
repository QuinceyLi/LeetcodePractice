# @lcpr-before-debug-begin
from python3problem35 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=35 lang=python3
# @lcpr version=30204
#
# [35] 搜索插入位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
    # 闭区间写法
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # left,right = 0, n-1
        # if target < nums[left]: return 0
        # elif target > nums[right] : return n
        # while left < right:
        #     if nums[left] < target < nums[right]:
        #         pre = left
        #         left += max((right - left) // 2, 1)
        #     elif target == nums[left]: return left
        #     elif target == nums[right]: return right
        #     elif nums[left] > target:
        #         right, left = left, pre
        # return left 
        return lower_bound(nums, target)
# @lc code=end



#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#

