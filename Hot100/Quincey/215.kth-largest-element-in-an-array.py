#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []   # 将数组加入小顶堆，堆中维护当前值最大的k个数
        for num in nums:
            heapq.heappush(pq, num) # 当前元素入堆
            if len(pq) > k:
                heapq.heappop(pq)   # 堆中元素超过k个，弹出最小的那个
        return pq[0]    # 最后堆顶的即为第k大的数
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

