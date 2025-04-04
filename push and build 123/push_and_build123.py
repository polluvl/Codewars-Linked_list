from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    if head is None:
        return Node(data)
    temp = head
    head = data
    head.next = temp
    return Node(None)

def build_one_two_three():
    node = Node(1)
    curr = node
    for i in range(2, 4):
        temp = Node(i)
        curr.next = temp
        curr = curr.next
    return node
