#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        mA = 0
        while left < right:
            temp = min(height[left],height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            mA = max(temp,mA)
        return mA
# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

