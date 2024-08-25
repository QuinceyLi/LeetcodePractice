#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        left, right=0, 1
        temp_s = s[left]
        max_len=0
        while right<len(s):
            if s[right] in temp_s:
                left = left+temp_s.index(s[right])+1
            temp_s = s[left:right+1]
            max_len = max(max_len,len(temp_s))
            right+=1
            
        return max_len
    
    
        
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

