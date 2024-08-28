#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30204
#
# [239] 滑动窗口最大值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """超时"""
        # max_list = []
        # for i in range(len(nums)):
        #     j=min(len(nums),i+k)
        #     max_list.append(max(nums[i:j]))
        #     if j==len(nums):break
        # return max_list

        """参考答案"""
        from collections import deque
        deque = deque()
        res =[]
        n_len = len(nums)
        # 实现滑动窗口的同时遍历
        for i,j in zip(range(1-k, n_len+1-k), range(n_len)):
            # 删除 deque 中对应的 nums[i-1]
            # ❓ 为什么要做这一步？
            if i>0 and deque[0] == nums[i-1]:  
                deque.popleft()
            # 删除窗口中小于nums[j]的数据，保证数据递减
            while deque and deque[-1]<nums[j]:
                deque.pop()
            deque.append(nums[j])
            if i>=0: # 当窗口形成后，才记录最大值
                res.append(deque[0])
        return res

        
# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

