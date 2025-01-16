#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30204
#
# [84] 柱状图中最大的矩形
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # D = 0
        # for idx,h in enumerate(heights):
        #     l, r = idx-1, idx+1
        #     while l>=0:
        #         if heights[l]>=h:l -= 1
        #         else: break
        #     while r<=(len(heights)-1):
        #         if heights[r] >= h: r += 1
        #         else: break
        #     D = max(D, h*(r-l-1))
        # return D
        # 单调栈
        st = []
        n = len(heights)
        left = [-1] * n
        for idx,x in enumerate(heights):
            while st and x <= heights[st[-1]]:
                st.pop()
            if st: left[idx] = st[-1]
            st.append(idx)
        right = [n] * n
        st = []
        for i in range(n-1, -1, -1):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st: right[i] = st[-1]
            st.append(i)
        D = 0
        for h,l,r in zip(heights, left, right):
            D = max(D, h*(r-l-1))
        return D

# @lc code=end



#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#

