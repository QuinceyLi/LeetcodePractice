#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30204
#
# [283] 移动零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         head=0
#         tail=len(nums)
#         while head<tail:
#             if nums[head]==0:
#                 nums.insert(tail,0)
#                 nums.pop(head)
#                 tail-=1
#             else:
#                 head+=1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head,tail = 0,0
        while head<len(nums):
            if nums[head]!=0:
                nums[head],nums[tail] = nums[tail],nums[head]
                tail+=1
            head+=1

# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

