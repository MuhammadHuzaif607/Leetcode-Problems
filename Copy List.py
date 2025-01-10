class Node:
    def __init__(self,val=0,next=None,random=None) :
        self.val = val
        self.next = next
        self.random = random
        
def copy_list(head: Node):
    copy_lst = {}
    cur = head
    while cur:
        copy = Node(cur.val)
        copy_lst[cur] = copy
        cur = cur.next
        
    cur = head
    while cur:
        copy = copy_lst[cur]
        copy.next = copy_lst[cur.next]
        copy.random = copy_lst[cur.random]
        cur = cur.next
        
    