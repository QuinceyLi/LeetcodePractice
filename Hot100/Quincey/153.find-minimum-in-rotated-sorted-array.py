#
# @lc app=leetcode.cn id=153 lang=python3
# @lcpr version=30204
#
# [153] 寻找旋转排序数组中的最小值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]
# @lc code=end



#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,15,17]\n
# @lcpr case=end

#

