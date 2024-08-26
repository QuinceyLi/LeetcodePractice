# @lcpr-before-debug-begin
from python3problem42 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def bianli(self,height,container,reverse):
        if not reverse:
            current_H = height[0] # 当前最大高度
            for i in range(1,len(height)):
                deltah = current_H - height[i]
                if deltah> 0 :
                    for j in range(deltah):
                        container[i][j] = 1
                        # print(container)
                elif deltah < 0 :
                    current_H = height[i]
                
        else:
            current_H = height[-1]
            for i in range(len(height)-1,-1,-1):
                deltah = current_H - height[i]
                if deltah> 0 :
                    for j in range(deltah):
                        container[i][j] = 1
                elif deltah < 0 :
                    current_H = height[i]
        return container

    # def trap(self, height: List[int]) -> int:
    #     # 动态规划
    #     M,L = max(height)-min(height),len(height)
    #     # container1 = [[0] * M] * L # 错误创建方法，浅拷贝，当container[0][j]被赋值,container[i][j]会被赋同样的值
    #     container1 = [[0]*M for i in range(L)]
    #     container2 = [[0]*M for i in range(L)]
    #     # print(container1)
    #     # 从左到右
    #     container1 = self.bianli(height,container1,False)
    #     # 从右到左
    #     container2 = self.bianli(height,container2,True)
    #     # print(container1,'\n',container2)

    #     yushui = sum([s1 for k1,k2 in zip(container1,container2) for s1,s2 in zip(k1,k2) if s1==s2==1 ])
    #     return yushui
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n  # pre_max[i] 表示从 height[0] 到 height[i] 的最大值
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n  # suf_max[i] 表示从 height[i] 到 height[n-1] 的最大值
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h  # 累加每个水桶能接多少水
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

