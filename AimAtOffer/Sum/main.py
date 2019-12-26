# -*- coding:utf-8 -*-
'''
class Solution:
    def Sum_Solution(self, n):
        # write code here
        if(n == 1):    # 不能用if的...
            return 1
        return (pow(n, 2) + n) >> 1
'''
class Solution:
    def Sum_Solution(self, n):
        # write code here
        ans = n
        temp = ans and self.Sum_Solution(n - 1)
        ans = ans + temp
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.Sum_Solution(5))