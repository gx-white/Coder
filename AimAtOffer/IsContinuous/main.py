# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        length = len(numbers)

        # 先找到除零之外的最大最小值
        min_num = 20
        max_num = 0
        count = 0
        i = 0
        while(i < length):
            if(numbers[i] == 0):
                count += 1
                i += 1
                continue
            if(min_num > numbers[i]):
                min_num = numbers[i]
            if(max_num < numbers[i]):
                max_num = numbers[i]

            i += 1
        if(count == 4):   # 处理四张大小王的情况
            return True
        diff = max_num - min_num
        if(diff == 0):    # 
            return False
        if(diff > length - 1):
            return False
        elif(diff == length - 1):
            return True
        else:
            if(diff < length - 1 - 4):   # 由于抽到的肯定是5张牌，所以这个其实是永远不会成立的
                return False
            else:
                return True
if __name__ == '__main__':
    sol = Solution()
    print(sol.IsContinuous([1,0,0,1,0]))