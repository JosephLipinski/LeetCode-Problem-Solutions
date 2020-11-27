# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class SinglyLinkedList:
    import copy
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_over = False
        total = l1.val + l2.val
        if total >= 10:
            carry_over = True
            head = ListNode(total % 10)
        else:
            head = ListNode(total)
            
        if (l1.next != None and l2.next != None):
            l1 = l1.next
            l2 = l2.next
            if carry_over:
                l1.val = l1.val + 1
            head.next = self.addTwoNumbers(l1, l2)
        elif (l1.next != None):
            l1 = l1.next
            l2 = ListNode(0)
            if carry_over:
                l1.val = l1.val + 1
            head.next = self.addTwoNumbers(l1, l2)
        elif (l2.next != None):
            l1 = ListNode(0)
            l2 = l2.next
            if carry_over:
                l1.val = l1.val + 1
            head.next = self.addTwoNumbers(l1, l2)
        else:
            if carry_over:
                head.next = ListNode(1)
        
        return head