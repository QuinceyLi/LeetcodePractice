#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30204
#
# [49] 字母异位词分组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 我的解法，超时
        # res = []
        # while len(strs) > 0: # 用for str1 in strs,strs=['bat']的时候迭代停止
        #     str1 = strs[0]
        #     ht1 = {k:str1.count(k) for k in set(str1)}
        #     templs = [str1]            
        #     strs.remove(str1)
        #     for str2 in strs[:]:
        #         ht2 = {k:str2.count(k) for k in set(str2)}
        #         if ht2==ht1:
        #             templs.append(str2)
        #             strs.remove(str2)
        #     res.append(templs)
        # return res
        d = defaultdict(list)
        #defaultdict 在试图访问一个不存在的键时，不会抛出 KeyError，而是直接生成一个默认值。
        #这里的 defaultdict(list) 表示当访问一个不存在的键时，会自动为这个键生成一个空列表。
        for s in strs:
            d[''.join(sorted(s))].append(s)  # sorted(s) 相同的字符串分到同一组
        return list(d.values())
# @lc code=end



#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

