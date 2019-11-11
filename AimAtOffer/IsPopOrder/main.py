# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.x = []

    def IsPopOrder(self, pushV, popV):
        # write code here
        self.x.append(pushV[0])
        pushV = pushV[1:]
        while(pushV):
            if(pushV[0] == popV[0]):
                pushV.pop(0)
                popV.pop(0)
            else:
                if(popV[0] == self.x[-1]):
                    popV.pop(0)
                    self.x.pop()
                else:
                    self.x.append(pushV[0])
                    pushV.pop(0)
        if(self.x == popV[::-1]):   # 判断剩下的部分是不是按照先入后出的顺序pop的
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    result = sol.IsPopOrder([1,2,3,4,5], [4,3,5,1,2])
    if(result):
        print('yes')
    else:
        print('no')

