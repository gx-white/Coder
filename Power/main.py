# -*- coding:utf-8 -*-
'''
class Solution:
    def Power(self, base, exponent):
        # write code here
        return pow(base, exponent)
'''
'''
# 这种结果是错的...但是不知道为什么提交上去也是可以通过的
class Solution:
    def Power(self, base, exponent):
        # write code here
        res=base
        flag=1
        if exponent<0:
            exponent*=-1
            flag=-1
        elif exponent==0:
            return 1
        while True:
            if exponent==1:
                res*=base
                break
            res*=res
            exponent = exponent//2
        return res if flag==1 else 1/res
'''

# 快速幂
class Solution:
    def Power(self, base, exponent):
        # write code here
        result = 1
        flag = 0
        if(exponent < 0):
            flag = 1
            exponent = -1 * exponent
        while(exponent > 0):
            if(exponent & 1):  # 奇数
                result = result * base
            base = base * base
            exponent = exponent >> 1   # 减半
        return result if flag == 0 else 1.0/result

if __name__ == "__main__":
    sol = Solution()
    print(sol.Power(2, 12))