# @lcpr-before-debug-begin
from python3problem739 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30204
#
# [739] 每日温度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # hx = {}
        # ans = []
        # pos = []
        # tt = temperatures[::-1]
        # M = 0
        # for idx, t in enumerate(tt):
        #     if t >= M:
        #         ans.append(0)
        #         M = t
        #     else:
        #         for i in range(t+1, M+1):
        #             if hx.get(i,-1) >= 0: 
        #                 pos.append(hx[i])
        #         ans.append(idx - max(pos))
        #         pos = []
        #     hx[t] = idx

        # return ans[::-1]
        # 单调栈
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans

# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#

