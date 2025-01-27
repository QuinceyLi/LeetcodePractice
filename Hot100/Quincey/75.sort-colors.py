#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30204
#
# [75] 颜色分类
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hx = {0:0,1:0,2:0}
        for n in nums:
            hx[n] += 1
        nums[0:hx[0]] = [0] * hx[0]
        nums[hx[0]:hx[0]+hx[1]] = [1] * hx[1]
        nums[hx[0]+hx[1]: hx[0]+hx[1]+hx[2]] = [2]*hx[2]
        
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

