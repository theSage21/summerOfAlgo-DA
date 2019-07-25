# Delte a node
class Solution:
    def deleteNode(self,node):
        cur = node
        while cur.next != None:
            prev = cur
            cur.val = cur.next.val
            cur = cur.next
        prev.next = None

