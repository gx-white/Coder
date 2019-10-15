# -*- coding:utf-8 -*-
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        length = len(s)
        m = ''
        for i in range(0, length):
            if(s[i] == ' '):
                m += '%20'
            else:
                m += s[i]
        return m
'''

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ', '%20')