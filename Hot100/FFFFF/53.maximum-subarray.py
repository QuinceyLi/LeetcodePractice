#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 超时
        # pre_sum = [0]
        # # diff = [0]
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     curr= nums[i]

        #     pre_sum.append(pre_sum[-1]+curr)

        #     sum_diff = [pre_sum[-1]-x for x in pre_sum[:-1]]
        #     max_sum = max(max_sum,max(sum_diff))
        #     # for j in range(len(sum_diff)):
        #     #     if sum_diff[j]<=0:
        #     #         pre_sum=pre_sum[j:]
        # return max_sum
    
        # 看了思路后
        max_sum = nums[0]
        pre_sum = nums[0]
        for num in nums[1:]:
            if pre_sum<0:
                pre_sum = num
            else:
                pre_sum = pre_sum+num
            max_sum = max(max_sum,pre_sum)
        return max_sum





# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

