#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30204
#
# [121] 买卖股票的最佳时机
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # for i in range(len(prices)-1):
        #     profit = max(profit, max(prices[i:])-prices[i])
        # return profit
        D = prices[-1]
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > D: D = prices[i]
            elif prices[i] < D: profit = max(profit, D- prices[i])
        return profit

# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

