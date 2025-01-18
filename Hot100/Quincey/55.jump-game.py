# @lcpr-before-debug-begin
from python3problem55 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30204
#
# [55] 跳跃游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置  
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i
# @lc code=end



#
# @lcpr case=start
# [5,9,3,2,1,0,2,3,3,1,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,0]\n
# @lcpr case=end

#

