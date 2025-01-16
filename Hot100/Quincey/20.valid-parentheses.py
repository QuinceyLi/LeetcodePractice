#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        khmap = {'(':')', '[':']', '{':'}'}
        for k in s:
            if k in khmap.keys(): stack.append(k)
            else:
                if not stack:return False 
                else:
                    zk = stack.pop()
                    if not khmap[zk] == k: return False
        return True if not stack else False

# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#

