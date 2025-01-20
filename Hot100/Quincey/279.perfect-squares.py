# @lcpr-before-debug-begin
from python3problem279 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30204
#
# [279] 完全平方数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# class Solution:
#     def numSquares(self, n: int) -> int:
        # bag = [x ** 2 for x in range(1, int(sqrt(n))+1)]
        # print(bag)
        # @cache
        # def dfs(k,c):
        #     if k < 0:
        #         return 0 if c == 0 else inf
        #     if bag[k] > c:
        #         return dfs(k-1, c)
        #     return min(dfs(k-1,c), dfs(k, c-bag[k])+1)
        
        # return dfs(len(bag)-1, n)
# 写在外面，多个测试数据之间可以共享，减少计算量
@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
def dfs(i: int, j: int) -> int:
    if i == 0:
        return inf if j else 0
    if j < i * i:
        return dfs(i - 1, j)  # 只能不选
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)  # 不选 vs 选

class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n)
# @lc code=end



#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#

