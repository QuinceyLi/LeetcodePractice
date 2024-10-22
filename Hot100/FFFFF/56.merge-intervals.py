#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ordered_intervals = sorted(intervals)
        res = []
        start,end = ordered_intervals[0][0],ordered_intervals[0][1]
        for inter in ordered_intervals:
            if inter[0]<=end:
                end = max(end,inter[1])
            else:
                res.append([start,end])
                start = inter[0]
                end = inter[1]
            if inter == ordered_intervals[-1] and [start,end] not in res:
                res.append([start,end])
        return res
            
            


# @lc code=end



#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#

