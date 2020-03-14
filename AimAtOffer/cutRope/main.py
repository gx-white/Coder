# -*- coding:utf-8 -*-
'''
题目描述
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）
输出描述:
输出答案。
示例： 输入 8 输出 18

思路：
我感觉应该是要均分才比较好
突然觉得行测还是有用的哈

这个题目大家都是用动态规划做的，明天再学习吧
'''
class Solution:
    def cutRope(self, number):
        # write code here
        if(number == 0) | (number == 1):
            return 0
        if(number == 2):
            return 1
        
        max_mutiply = 1
        flag = False
        for i in range(2, number):
            shang = number / i
            yu = number % i
            table = [shang for m in range(0, i)]
            for j in range(0, yu):
                table[j] += 1
            mutiply = 1
            for each in table:
                mutiply *= each
            if(mutiply > max_mutiply):
                max_mutiply = mutiply
                flag = True
            else:
                if(flag == True):
                    break
        return max_mutiply

if __name__ == "__main__":
    sol = Solution()
    print(sol.cutRope(8))