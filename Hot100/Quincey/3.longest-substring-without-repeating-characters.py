# @lcpr-before-debug-begin
from python3problem3 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s:
        #     window = {s[0]:0}
        # else:
        #     return 0
        # i = 1
        # L = 1
        # while i < len(s):
        #     for v in window:
        #         if v != s[i]:continue
        #         else:
        #             i = window[v] + 1
        #             L = max(len(window), L)
        #             window={}
        #             break
        #     window[s[i]] = i
        #     i += 1
        # return max(len(window),L)
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res
            
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

