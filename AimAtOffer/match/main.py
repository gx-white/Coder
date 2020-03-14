# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        len_p = len(pattern)
        len_s = len(s)

        if((len_p == 0) & (len_s == 0)):
            return True
        if(len_p == 0):
            return False
        
        if(len_p > 1):
            if(pattern[1] == '*'):
                if(len_s > 0):
                    if(s[0] == pattern[0]) | (pattern[0] == '.'):
                        return self.match(s, pattern[2:]) | self.match(s[1:], pattern[2:]) | self.match(s[1:], pattern)
                    else:
                        return self.match(s, pattern[2:])
                else:
                    return self.match(s, pattern[2:])
        if(len_s > 0):
            if((s[0] == pattern[0]) | (pattern[0] == '.')):
                return self.match(s[1:], pattern[1:])
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.match("aaa", "ab*ac*a"))