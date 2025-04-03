'''convert to string task'''
class Node():
  """initializing a node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
  """a function to make a string out of Node"""
    outp = []
    temp = node
    while temp:
        outp.append(str(temp.data))
        temp = temp.next
    if temp is None:
        outp.append('None')
    return ' -> '.join(outp)
