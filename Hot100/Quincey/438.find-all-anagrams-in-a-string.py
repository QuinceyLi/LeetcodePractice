# @lcpr-before-debug-begin
from python3problem438 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        L = len(p)
        left = 0
        right = len(s) - L + 1
        p = sorted(p)
        res = []
        while left <= right:
            if sorted(s[left:left+L]) == p:
                res.append(left)
            left += 1
        return res

# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

