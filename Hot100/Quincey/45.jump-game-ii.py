#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # bushu = [x for x in range(len(nums))]
        # for idx, val in enumerate(nums):
        #     for nxt in range(idx+1, idx+val+1):
        #         if nxt < len(nums):
        #             bushu[nxt] = min(bushu[nxt], bushu[idx]+1)
        # return bushu[-1]
        ans = 0
        cur_right = 0  # 已建造的桥的右端点
        next_right = 0  # 下一座桥的右端点的最大值
        for i in range(len(nums) - 1):
            next_right = max(next_right, i + nums[i])
            if i == cur_right:  # 到达已建造的桥的右端点
                cur_right = next_right  # 造一座桥
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

