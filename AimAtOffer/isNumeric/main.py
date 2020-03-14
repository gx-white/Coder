# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # "12e","1a3.14","1.2.3","+-5"和"12e+4.3"
        length = len(s)
        if(length == 0):
            return False
        has_sign = False
        has_point = False
        has_e = False

        for i in range(0, length):
            if((s[i] == 'E') | (s[i] == 'e')):
                if(has_e):
                    return False
                has_e = True
                if(i == length-1):  # e不能出现在最后一个
                    return False
            elif((s[i] == '+') | (s[i] == '-')):
                if(has_sign):
                    if((s[i-1] != 'e') & (s[i-1] != 'E')):  #
                        return False
                has_sign = True
                if((i > 0) & (s[i-1] != 'e') & (s[i-1] != 'E')):
                    return False
            elif(s[i] == '.'):
                if(has_point | has_e):
                    return False
                has_point = True
            else:
                if((s[i] < '0') | (s[i] > '9')):
                    return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isNumeric("-1E-16"))
