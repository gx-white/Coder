# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        length = len(s)
        if(length == 0):
            return 0

        flag = 1
        if(s[0] == '-'):
            flag = -1
            s = s[1:]
        elif(s[0] == '+'):
            s = s[1:]
        
        num = 0
        table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for each in s:
            if(each not in table):
                return 0
            num = (num << 1) + (num << 3) + (ord(each) & 0xf)   # 这里每个都要加括号，要不然会计算错误
        return num * flag

if __name__ == "__main__":
    sol = Solution()
    print(sol.StrToInt('-2147483648'))