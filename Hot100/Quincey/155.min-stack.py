#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30204
#
# [155] 最小栈
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MinStack:

    def __init__(self):
        self.ms = []
        self.min = []

    def push(self, val: int) -> None:
        self.ms.append(val)
        if not self.min or val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.ms.pop()
        self.min.pop()

    def top(self) -> int:
        return self.ms[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end



#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#

