# -*- coding:utf-8 -*-
'''
# 错误的思路
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        length = len(numbers)
        numbers.sort()  # 先整体按数字大小降序排列
        for i in range(0, length):
            numbers[i] = str(numbers[i])
        numbers = numbers[::-1]
        result = []
        i = 0
        while(1):
            if(len(numbers[i]) != len(numbers[i+1])):
                # 说明到了位数不同的临界处了
                result += numbers[0:i+1][::-1]
                numbers = numbers[i+1:]
                if(len(numbers) == 1):
                    result += numbers
                    break
                elif(len(numbers) == 0):
                    break
                i = 0
                continue
            i = i + 1
            if(i == (len(numbers)-1)):
                result += numbers[0:i+1][::-1]
                break
        temp = ''
        for each in result:
            temp += each
        return int(temp)
'''
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        length = len(numbers)
        if(length == 0):
            return ""
        for i in range(0, length):
            numbers[i] = str(numbers[i])

        for i in range(0, length):
            min_str = numbers[i]
            min_index = i
            for j in range(i+1, length):
                if(self.compare(min_str, numbers[j])):
                    min_str = numbers[j]
                    min_index = j
            if(min_index != i):
                temp = numbers[i]
                numbers[i] = numbers[min_index]
                numbers[min_index] = temp
        result = ''
        for each in numbers:
            result += each
        return int(result)

    def compare(self, s1, s2):
        if(int(s1+s2) > int(s2+s1)):
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.PrintMinNumber([321,32,3]))