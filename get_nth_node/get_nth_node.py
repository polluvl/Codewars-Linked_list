class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """a function to get a node with a given index

    Args:
        node (Node): Node object
        index (int): index of a node

    Raises:
        ValueError: if given index brings errors or node is wrong

    Returns:
        Node: a Node object at that position
    """
    if not isinstance(index, int) or index < 0 or node == Node:
        raise ValueError
    counter = 0
    temp = node
    while temp:
        if index == counter:
            return temp
        temp = temp.next
        counter +=1
    raise ValueError
  
