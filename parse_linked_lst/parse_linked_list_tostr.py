'''linked_list_from_string'''
class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


def linked_list_from_string(s):
    if s == 'None':
        return None
    spl = s.split(' -> ')[:-1]

    head = Node(int(spl[0]))
    temp = head
    for k in spl[1:]:
        temp.next = Node(int(k))
        temp = temp.next
    return head
