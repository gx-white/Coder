# -*- coding:utf-8 -*-
'''
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        length = len(s)
        if(length == 0):
            return ""
        if(n == length):
            return s
        elif(n > length):
            n = n % length

        return s[n:] + s[0:n]
'''
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        length = len(s)
        s = list(s)
        if(length == 0):
            return ""
        n = n % length
        self.swap(s, 0, n-1)
        self.swap(s, n, length-1)
        self.swap(s, 0, length-1)
        return "".join(s)

    def swap(self, s, start, end):
        while(start < end):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.LeftRotateString('abc', 1))

