# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        return num1 if (num2 == 0) else self.Add((num1 ^ num2)&0xffffffff, ((num1 & num2) << 1)&0xffffffff)

if __name__ == "__main__":
    sol = Solution()
    print(sol.Add(-2, 3))