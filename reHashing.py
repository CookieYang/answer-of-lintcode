class ListNode(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def rehashing(hashTable):
    capcity = len(hashTable)
    newHash = [None] * 2 * capcity
    for i in  range(capcity):
        head = hashTable[i]
        while head != None:
            value = head.val
            pos = value % (2 * capcity)
            if newHash[pos] == None:
                # create new list
                newHash[pos] = ListNode(value)
            else:
                nHead = newHash[pos]
                while nHead.next != None:
                    nHead = nHead.next
                nHead.next = ListNode(value)
            head = head.next
    return newHash

a = ListNode(5)
b = ListNode(29,a)
c = [None,None,b]
print(rehashing(c))