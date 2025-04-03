class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
  """a function to mode a first node of source to the beginning of dest"""
    if source:
        to_move = source
        source = to_move.next
        second = dest
        dest = to_move
        to_move.next = second
    else:
        raise ValueError
    
    return Context(source, dest)
