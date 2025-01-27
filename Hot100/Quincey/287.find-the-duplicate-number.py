# @lcpr-before-debug-begin
from python3problem287 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30204
#
# [287] 寻找重复数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(len(nums)):
        #     if nums[i] != i+1: 
        #         if nums[i] == nums[nums[i]-1]: return nums[i]
        #         else:
        #             tmp = nums[nums[i]-1]
        #             nums[nums[i]-1] = nums[i]
        #             nums[i] = tmp
        #     else: pass
        # return nums[-1]

        # now_ind=1
        # n=len(nums)-1
        # count=0
        # while now_ind<=n and count<n:
        #     while nums[now_ind]!=now_ind:
        #         if nums[nums[now_ind]]==nums[now_ind]:  # 之前已经填过
        #             return nums[now_ind]
        #         nums[nums[now_ind]], nums[now_ind]=nums[now_ind],nums[nums[now_ind]]
        #         count+=1
        #     now_ind+=1
        # return nums[0]

        # 快慢指针
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow,fast = nums[slow],nums[nums[fast]]
        pre = 0
        while pre != slow:
            pre,slow = nums[pre], nums[slow]
        return pre

# @lc code=end



#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#

