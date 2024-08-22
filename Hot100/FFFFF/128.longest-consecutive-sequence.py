# @lcpr-before-debug-begin
from python3problem128 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30204
#
# [128] 最长连续序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# import numpy as np
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums)<2:
#             return len(nums)
#         sort_nums = np.unique(sorted(nums))
#         max_len = 1
#         temp_len = 1
#         for i in range(1,len(sort_nums)):
#             if sort_nums[i]-sort_nums[i-1]==1:
#                 temp_len+=1
#                 if temp_len>max_len:
#                     max_len=temp_len
#             else:
#                 temp_len=1
#         return max_len
    


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        temp_len = 1 
        nums = set(nums)
        for num in nums:
            if num-1 in nums:
                continue
            else:
                acc_num=1
                while num+acc_num in nums:
                    temp_len+=1
                    acc_num+=1
                if temp_len > max_len:
                    max_len = temp_len
                temp_len=1
        return max_len
# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

#

