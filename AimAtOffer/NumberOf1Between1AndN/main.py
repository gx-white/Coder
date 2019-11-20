# -*- coding:utf-8 -*-
'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n+1):
            temp = i
            while(temp):
                if(temp % 10 == 1):
                    count += 1
                temp = temp / 10
        return count
'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        base = 10
        temp = n
        while(temp):
            num = temp % 10
            temp = n / base
            if(num > 1):   # 可以改成对应要计算的数字
                count += (temp + 1) * base / 10
            elif(num < 1):
                count += temp * base / 10
            else:
                count += temp * base / 10 + n % (base / 10) + 1
            base *= 10
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.NumberOf1Between1AndN_Solution(2134))