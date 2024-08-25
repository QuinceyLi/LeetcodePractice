#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
        
#         left,right = 0,0
#         max_area = 0
#         for left in range(len(height)):
#             for right in range(left,len(height)):
#                 left_h = height[left]
#                 right_h = height[right]
#                 temp_area = (right-left)*min(right_h,left_h)
#                 if temp_area>max_area:
#                     max_area = temp_area
#         return max_area

class Solution:
    def maxArea(self, height: List[int]) -> int: 
        left = 0
        right = len(height)-1
        max_area = 0
        while left<right:
            left_height = height[left]
            right_height = height[right]
            temp_area = (right-left)*min(left_height,right_height)
            max_area = max(temp_area,max_area)
            if right_height<=left_height:
                right-=1
            else:
                left+=1
        return max_area
    
# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

