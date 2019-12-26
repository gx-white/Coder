# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        length = len(s)
        s = list(s)

        # 翻转整个字符串
        begin = 0
        end = length - 1
        while(begin < end):
            temp = s[begin]
            s[begin] = s[end]
            s[end] = temp
            begin += 1
            end -= 1
        
        # 翻转每个单词
        begin = 0
        end = begin + 1
        while(end < length):
            while(s[end] != ' '):
                end += 1
                if(end == length):
                    break
            end -= 1
            temp_index = end
            while(begin < end):
                temp = s[begin]
                s[begin] = s[end]
                s[end] = temp
                begin += 1
                end -= 1
            begin = temp_index + 2
            end = begin + 1

        return ''.join(s)

if __name__ == '__main__':
    sol = Solution()
    print(sol.ReverseSentence('student. a am I'))