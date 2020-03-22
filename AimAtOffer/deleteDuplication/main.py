# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if(pHead == None):
            return pHead
        if(pHead.next == None):
            return pHead
        head = ListNode(1)
        head.next = pHead
        pre = head
        last = head.next
        while(last != None):
            if(last.next != None):
                if(last.next.val == last.val):
                    while(last.next.val == last.val):
                        last = last.next
                        if(last.next == None):
                            break
                    pre.next = last.next
                    last = last.next
                else:
                    pre = pre.next
                    last = last.next

            else:
                break

        return head.next
        
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node7 = ListNode(5)
    node8 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    sol = Solution()
    node = sol.deleteDuplication(node1)
    while(node != None):
        print(node.val)
        node = node.next