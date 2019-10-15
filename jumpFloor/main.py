# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.save = [0, 1, 2]

    def jumpFloor(self, number):
        # write code here
        if(number <= 2):
            return self.save[number]

        try:
            a = self.save[number - 1]
        except:
            a = self.jumpFloor(number - 1)
            self.save.append(a)
        try:
            b = self.save[number - 2]
        except:
            b = self.jumpFloor(number - 2)
            self.save.append(b)
        
        return a + b

if __name__ == "__main__":
    sol = Solution()
    print(sol.jumpFloor(3))