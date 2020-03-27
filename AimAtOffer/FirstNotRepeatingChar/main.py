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
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        length = len(s)
        if(length == 0):
            return -1
        result = [-1 for i in range(0, 255)]
        for i in range(0, length):
            if(result[ord(s[i])] == -1):
                result[ord(s[i])] = i
            elif(result[ord(s[i])] > -1):
                result[ord(s[i])] = -2
            else:
                pass
        min_value = 10000000000
        min_index = -1
        for i in range(0, 255):
            if(result[i] > -1):
                if(result[i] < min_value):
                    min_value = result[i]
                    min_index = i
        if(min_index != -1):
            return result[min_index]
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.FirstNotRepeatingChar('google'))