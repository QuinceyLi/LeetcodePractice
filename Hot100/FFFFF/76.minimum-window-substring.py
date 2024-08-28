#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # res = ''
        # cha_len = ord("z")-ord("A")
        # cha = [0]*cha_len
        
        # l,r=0,0
        # n = len(s)
        # cha_t = [0]*cha_len
        # if len(s)==0: return ''

        # for _t in t:
        #     cha_t[ord(_t)-ord('A')]+=1

        # while l < n and r<n:
        #     # print("111",s[l:r+1])
        #     if s[r] in t:
        #         # print(r,s[l:r+1])
        #         cha[ord(s[r])-ord('A')]+=1
        #         if all([True  if x-y>=0 else False for x,y in zip(cha,cha_t)]):
        #             res = s[l:r+1] if len(s[l:r+1])<len(res) or res=='' else res
        #             cha[ord(s[l])-ord('A')]-=1
        #             l+=1
        #             while l<=r and s[l] not in t:
        #                 l+=1
        #     if r<n:
        #         r+=1
        # return res
    
        need = defaultdict(int)
        for c in t:
            need[c]+=1
        res = ''
        need_len = len(t)

        l=0
        for r,c in enumerate(s):
            
            if need[c]>0:
                need_len -= 1
            need[c] -=1
            if need_len == 0:  #步骤一：滑动窗口包含了所有T元素
                while l<=r:     #步骤二：增加i，排除多余元素
                    cc = s[l]
                    if need[cc]==0:
                        break
                    need[cc] += 1
                    l+=1
            
                if res =='' or len(res)>(r-l):
                    res = s[l:r+1]
                
                need[s[l]] += 1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                need_len +=1
                l+=1
        return res

                
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

