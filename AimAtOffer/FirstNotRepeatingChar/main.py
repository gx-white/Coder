# -*- coding:utf-8 -*-
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        length = len(s)
        if(length == 0):
            return -1
        for i in range(0, length):
            if(s[i] in s[0:i] + s[i+1 :]):
                continue
            else:
                break
        return i
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        length = len(s)
        if(length == 0):
            return -1
        result = {}
        for each in s:
            try:
                result[each] += 1
            except:
                result[each] = 1
        for i in range(0, length):
            if(result[s[i]] == 1):
                return i


if __name__ == "__main__":
    sol = Solution()
    print(sol.FirstNotRepeatingChar('google'))