class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    temp = head
    if not head:
        return None
    while temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        temp = temp.next
    return head
