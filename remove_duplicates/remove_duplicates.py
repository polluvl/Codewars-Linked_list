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
    if temp.next == None:
        return head
    while temp and temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
