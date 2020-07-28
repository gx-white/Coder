import sys
"""
def main():
    num = sys.stdin.readline().strip()
    [n, m] = map(int, num.split())
    lines = sys.stdin.readline().strip()
    values = map(int, lines.split())
    values.sort()
    Q = int(sys.stdin.readline().strip())
    '''
    for i in range(0, Q):
        q = int(sys.stdin.readline().strip())
        sub = values[0:q]
        
        result = 0
        j = 1
        while(len(sub) > 0):
            for i in range(0, m):
                result += sub[-1] * j
                sub.pop()
                if(len(sub) <= 0):
                    break
            j += 1
        print result
    '''
    for i in range(0, Q):
        q = int(sys.stdin.readline().strip())
        result = 0
        sub = values[:q][::-1]
        j = 1
        while(q > m):
            q -= m
            result += j * sum(sub[:m])
            sub = sub[m:]
            j += 1
        if(len(sub) > 0):
            result += j * sum(sub)
        print(result)
        

if __name__ == "__main__":
    main()
"""
'''
class Solution(object):
    def __init__(self):
        self.result = []
        self.current_can = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        length = len(candidates)
        self.back(candidates, target, length)
        return self.result

    def back(self, candidates, target, length):
        sum_ = 0
        for i in range(0, length):
            sum_ += candidates[i]
            self.current_can.append(candidates[i])
            if(sum_ == target):
                self.result.append([i for i in self.current_can])
                sum_ = 0
                self.current_can = []
            elif(sum_ > target):
                self.current_can.pop()
                sum_ -= candidates[i]
                if(sum_ == 0):
                    break
                self.back(candidates, target-sum_, length)
                break
def main():
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
    

if __name__ == "__main__":
    print(main())
'''
import threading
from threading import Thread
import time

def func(n):
    print('Thread %s is running...' % threading.currentThread().name)
    for i in range(0, n):
        print('Thread %s is running: %d' % (threading.currentThread().name, i))
        time.sleep(3)
    print('Thread %s ended' % threading.currentThread().name)

t = Thread(target=func, name='thread1', args=(5,))
t.start()
print('Thread %s ended' % threading.currentThread().name)