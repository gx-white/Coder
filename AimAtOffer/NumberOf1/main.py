# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        '''
        if(n < 0):
            n = n & 0xffffffff   # python中求负数的补码  bin(n & 0xffffffff)
            # 注意，使用java或者c++写时不需if判断，因为他两默认转的就是补码形式，而python不是
        '''
        count = 0
        while(n):
            count += 1
            # 常见妙用方式
            n = n & (n - 1)   # 重复操作，有多少个1，这个操作就可以执行多少次
            print(n)
            break
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.NumberOf1(-1))
                