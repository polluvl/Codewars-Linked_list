class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """
    a function which inserts a node into the 
    correct location of a pre-sorted linked 
    list which is sorted in ascending order. 
    """
    if head is None or head.data > data:
        k = Node(data)
        k.next = head
        return k
    temp = head
    while temp:
        k = Node(data)
        if temp.next:
            if temp.next.data > k.data:
                k.next = temp.next
                temp.next = k
                return head
        temp = temp.next
        if temp.next is None:
            temp.next = k
            return head


    raise ValueError
