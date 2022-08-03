# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def insert(head, val):
        tempNode = head
        newNode = ListNode(val)
        while(True):
            if(tempNode.next == None):
                tempNode.next = newNode
                break
            tempNode = tempNode.next

class Solution(object):
    def middleNode(self, head):
        count = 0
        tempNode = head
        while(True):
            count += 1
            if(tempNode.next == None):
                break
            tempNode = tempNode.next
        middle = (int)(count/2)+1

        count = 0
        tempNode = head
        while(True):
            count += 1
            if(count == middle):
                head = tempNode
                return head
            if(tempNode.next == None):
                break            
            tempNode = tempNode.next
            
s1 = Solution()
node = ListNode(1)

node.insert(2)
node.insert(3)
node.insert(4)
node.insert(5)
node.insert(6)

s1.middleNode(node)
