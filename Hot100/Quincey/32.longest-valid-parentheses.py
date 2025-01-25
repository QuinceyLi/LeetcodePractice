#
# @lc app=leetcode.cn id=32 lang=python3
# @lcpr version=30204
#
# [32] 最长有效括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maxL = 0
        n = len(s)
        tmp = [0] * n
        cur = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()
                    tmp[i], tmp[j] = 1, 1
        for num in tmp:
            if num:
                cur += 1
            else:
                maxL = max(cur, maxL)
                cur = 0
        maxL = max(cur, maxL)
        return maxL

                

# @lc code=end



#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

#

