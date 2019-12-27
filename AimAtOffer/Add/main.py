# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while(num2):
            num1, num2 = ((num1 ^ num2) & 0xffffffff), ((num1 & num2) << 1)
        # result = num1 if (num2 == 0) else self.Add((num1 ^ num2), ((num1 & num2) << 1))
        if(num1 >> 31 != 0):
            # return num1 - pow(2, 32)
            return ~(num1 ^ 0xffffffff)   # 和上一句是一样的作用
        return num1

if __name__ == "__main__":
    sol = Solution()
    print(sol.Add(-2, -8))