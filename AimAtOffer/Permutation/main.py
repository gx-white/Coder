# -*- coding:utf-8 -*-
'''
class Solution:
    def __init__(self):
        self.arr = []
    def Permutation(self, ss):
        # write code here
        if(ss == ''):
            return ''
        if(len(ss) == 1):
            return [ss]
        # ss = sorted(ss)   # 先对字符串进行排序
        temp = ''
        self.digui(ss, temp)
        return sorted(self.arr)
        

    def digui(self, ss, temp):
        if(len(ss) == 0):
            if(temp not in self.arr):
                self.arr.append(a)
            return
        i = 0
        length = len(ss)
        while(i < length):
            temp += ss[i]
            self.digui(ss[0:i]+ss[i+1:], temp)
            temp = temp[0:-1]
            i = i + 1
'''
class Solution:
    def __init__(self):
        self.arr = []
    def Permutation(self, ss):
        # write code here
        if(ss == ''):
            return ''
        ss = sorted(ss)
        self.arr.append(''.join(ss))
        length = len(ss)
        while(True):
            fromIndex = length - 1
            for i in range(length-1, 0, -1):
                if(ss[i-1] < ss[i]):
                    break
                fromIndex -= 1
            if(fromIndex == 0):
                break
            changeIndex = fromIndex - 1

            for i in range(fromIndex, length):
                if(ss[i] <= ss[fromIndex-1]):    # 如果没有等于号，会在字符串中存在相同字符时死循环
                    break
                changeIndex += 1
            temp = ss[fromIndex-1]
            ss[fromIndex-1] = ss[changeIndex]
            ss[changeIndex] = temp
            ss = ss[0:fromIndex] + ss[fromIndex:][::-1]

            self.arr.append(''.join(ss))
        return self.arr

if __name__ == "__main__":
    sol = Solution()
    a = sol.Permutation('1223')
    print(a)