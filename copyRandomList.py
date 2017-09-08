# encoding:UTF-8
from structs import RandomListNode

def copyRandomList(head):
    p = head
    dest = RandomListNode(0)
    t = None
    # 复制节点并将新节点插入旧节点后面
    while p != None:
        t = RandomListNode(p.label)
        t.next = p.next
        t.random = p.random
        p.next = t
        p = t.next
    p = head
    # 更新新节点的random指针
    while p != None:
        t = p.next
        if t.random != None:
            t.random = t.random.next
        p = t.next
    p = head
    dest = p.next
    while p != None:
        t = p.next
        p.next = t.next
        p = t.next
        if p != None:
            t.next = p.next
    return dest

c = RandomListNode(3)
b = RandomListNode(2,c)
a = RandomListNode(1,b)
d = copyRandomList(a)
print(d)