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
        ## 求位数
        number = 1
        temp = n / 10
        while(temp):
            temp = temp / 10
            number += 1
        ## 
        count = 0
        for i in range(1, number+1):

        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.NumberOf1Between1AndN_Solution(1))