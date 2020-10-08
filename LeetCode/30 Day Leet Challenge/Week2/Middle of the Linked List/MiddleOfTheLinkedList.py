# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(self, head: ListNode) -> ListNode:
    curr=ListNode()
    curr=head
    count=0;
    while(curr.next!= None):
        curr=curr.next;
        count+=1
    i=0
    curr=head;
    while(i<count/2):
        curr=curr.next
        i+=1
    return curr;
