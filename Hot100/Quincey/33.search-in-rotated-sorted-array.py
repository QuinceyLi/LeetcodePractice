# @lcpr-before-debug-begin
from python3problem33 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30204
#
# [33] 搜索旋转排序数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    if l == len(nums) or nums[l] != target: return -1
    else: return l

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        if target <= nums[-1]:
            return -1 if lower_bound(nums[left:], target) < 0 else lower_bound(nums[left:], target) + left 
        else: 
            return lower_bound(nums[0:left], target)

# @lc code=end



#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4,5,1,2,3]\n1\n
# @lcpr case=end

#

