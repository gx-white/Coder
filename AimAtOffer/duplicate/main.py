# -*- coding:utf-8 -*-
'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        table = {}
        for each in numbers:
            if(each in table):
                duplication[0] = each
                return True
            table[each] = 1
        return False
'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        length = len(numbers)
        for i in range(0, length):
            if(numbers[i] == i):
                continue
            if(numbers[numbers[i]] == numbers[i]):
                duplication[0] = numbers[i]
                return True
            '''
            temp = numbers[numbers[i]]
            numbers[numbers[i]] = numbers[i]
            numbers[i] = temp
            '''
            numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
        return False