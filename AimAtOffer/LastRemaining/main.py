# -*- coding:utf-8 -*-
class Node:
    def __init__(self, x):
        self.value = x
        self.next = None
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if(n == 0):
            return -1
        head = Node(0)
        i = 1
        temp_head = head
        while(i < n):
            temp = Node(i)
            temp_head.next = temp
            temp_head = temp
            i += 1
        temp.next = head
        pre_node = temp

        count = n
        temp_m = -1
        while(count != 1):
            cur_node = pre_node.next
            temp_m += 1
            if(temp_m == m-1):
                pre_node.next = cur_node.next
                temp_m = -1
                count -= 1
                continue
            pre_node = cur_node
        return pre_node.value
            



if __name__ == '__main__':
    sol = Solution()
    print(sol.LastRemaining_Solution(5, 2))