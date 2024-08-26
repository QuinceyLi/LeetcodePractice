#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res_idx = []
        ch_p = {}
        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return res_idx
    
        for x in p:
            ch_p[x] = ch_p.get(x,0)+1
        for i in range(s_len-p_len+1):
            ch = {}
            if s[i] in p:
                for c in s[i:i+p_len]:
                    ch[c] = ch.get(c,0)+1
               
                if ch == ch_p:
                    res_idx.append(i)
        return res_idx

# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

