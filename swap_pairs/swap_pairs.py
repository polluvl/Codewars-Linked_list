from preloaded import Node

def swap_pairs(head):
    if not head:
        return None
    if not head.next:
        return head
    temp = head
    while temp:
        curr = temp
        new_first = temp.next
        new_first.next = curr
        temp = temp.next.next
    return head
