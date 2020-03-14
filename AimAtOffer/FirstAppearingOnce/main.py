# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.table = [-1 for i in range(128)]
        self.index = 0
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        min_value = 1000
        min_index = -1
        for i in range(0, 128):
            if(self.table[i] > -1):
                if(self.table[i] < min_value):
                    min_value = self.table[i]
                    min_index = i

        if(min_index > -1):
            return chr(min_index)
        return '#'
    def Insert(self, char):
        # write code here
        if(self.table[ord(char)] == -1):  # 说明是第一次出现
            self.table[ord(char)] = self.index
        elif(self.table[ord(char)] == -2):   # 说明已经出现多次了
            pass
        elif(self.table[ord(char)] > -1):
            self.table[ord(char)] = -2
        self.index += 1

