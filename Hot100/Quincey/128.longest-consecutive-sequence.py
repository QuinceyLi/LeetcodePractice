#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30204
#
# [128] 最长连续序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) > 0:
            hx = {}
            hx[nums[0]]=1
            for i in range(1,len(nums)):
                if (nums[i]-1 in hx):
                    if (nums[i]!=nums[i-1]):
                        hx[nums[i]] = hx[nums[i-1]] + 1
                    else:
                        hx[nums[i]] = hx[nums[i-1]]
                else:
                    hx[nums[i]] = 1
            return max(hx.values())
        else:
            return 0
# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

#

