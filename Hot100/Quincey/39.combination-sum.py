# @lcpr-before-debug-begin
from python3problem39 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30204
#
# [39] 组合总和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        path = []
        def dfs(cur_sum,newcandidates):
            if cur_sum == target:
                ans.append(path.copy())
                return 1
            elif cur_sum > target: return 2

            for c in newcandidates:
                path.append(c)
                res = dfs(sum(path), [x for x in newcandidates if x >= c])
                path.pop()
                if res == 2: return 


        dfs(0, candidates)
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

