'''linked_list_from_string'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
  """
  a function that takes a linked list 
  and returns a string out of it
  """
    outp = []
    temp = node
    while temp:
        outp.append(str(temp.data))
        temp = temp.next
    if temp is None:
        outp.append('None')
    return ' -> '.join(outp)


def linked_list_from_string(s):
  """a function that takes a linked list which was stringified 
  and returns a linked list again
  """
    if s == 'None':
        return None
    spl = s.split(' -> ')[:-1]

    head = Node(int(spl[0]))
    temp = head
    for k in spl[1:]:
        temp.next = Node(int(k))
        temp = temp.next
    return head
