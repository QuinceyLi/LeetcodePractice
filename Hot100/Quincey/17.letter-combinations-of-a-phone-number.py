#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Map = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        if not digits:return []
        ans = []
        n = len(digits)
        path = [''] * n
        def dfs(i):
            if i == n:
                ans.append(''.join(path.copy()))
                return
            for x in Map[int(digits[i])]:
                path[i] = x
                dfs(i+1)
        dfs(0)
        return ans
# @lc code=end



#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#

