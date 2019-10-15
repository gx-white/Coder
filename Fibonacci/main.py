# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.fib = [0, 1, 1]

    def Fibonacci(self, n):
        # write code here
        if((n == 0) | (n == 1) | (n == 2)):
            return self.fib[n]
        else:
            try:
                a = self.fib[n-1]
            except:
                a = self.Fibonacci(n-1)
                self.fib.append(a)
            try:
                b = self.fib[n-2]
            except:
                b = self.Fibonacci(n-2)
                self.fib.append(b)
            return a + b

if __name__ == "__main__":
    sol = Solution()
    print(sol.Fibonacci(5))