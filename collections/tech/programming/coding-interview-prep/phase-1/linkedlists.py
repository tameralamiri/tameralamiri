# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

# def solution(head, k):
#     if not head or k == 0:
#         return None
#     count = {}
#     dummy = ListNode(0)
#     dummy.next = head
#     curr = head
#     while curr:
#         if curr.value in count and count[curr.value] >= k: # Delete the node
#             if curr.next: 
#                 curr.value = curr.next.value
#                 curr.next = curr.next.next
#             else:
#                 curr.value = None
#                 curr.next = None
#         elif curr.value not in count:
#             count[curr.value] = 1 
#         else:
#             count[curr.value] += 1
#         curr = curr.next
#     print(count)
#     return dummy.next

# def print_ll(head):
#     while head:
#         print(str(head.value)+"->", end="")
#         head = head.next
#     print("None")


# def solution(head, k):
#     if not head or k <= 0:
#         return None

#     dummy = ListNode(0)
#     dummy.next = head
#     current = dummy
#     counts = {}

#     while current.next:
#         element = current.next.value
#         counts[element] = counts.get(element, 0) + 1

#         if counts[element] > k:
#             # Remove the node
#             current.next = current.next.next
#         else:
#             current = current.next

#     return dummy.next

# head = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(2)
# node4 = ListNode(2)
# head.next = node2
# node2.next = node3
# node3.next = node4
# print_ll(solution(head, 1))


# ###############
# def solution(head):
#     if not head:
#         return None
        
#     curr = head
#     insert_next = True
#     while curr:
#         if insert_next:
#             temp = curr.next
#             curr.next = ListNode(0, temp)
#             insert_next = not insert_next
#         curr = curr.next
    
        
#     return head

# def solution(head):
#     current = head
#     while current:
#         # Create a new node with value 0
#         zero_node = ListNode(0)
#         # Insert the zero node after the current node
#         zero_node.next = current.next
#         current.next = zero_node
#         # Move to the next original node in the list
#         current = zero_node.next
#     return head



##############

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def copy_list(head):
    dummy = ListNode(0)
    copy = dummy
    curr = head
    while curr:
        copy.next = ListNode(curr.value)
        copy = copy.next
        curr = curr.next
    return dummy.next
    
def solution(head):
    # reverse the list to a new copy
    # compare the new list to the old list
    # big o 3n
    
    copy = copy_list(head)
    reversed_copy = reverse_list(copy)
    
    curr = head
    rev_curr = reversed_copy
    
    
    
    while curr and rev_curr:
        if curr.value != rev_curr.value:
            return False
        curr = curr.next
        rev_curr = rev_curr.next
        
    return True
        
def print_ll(head):
    while head:
        print(str(head.value)+"->", end="")
        head = head.next

    print("None")

# linked list is a palindrome and to pass the test suite.

# Initialize a slow pointer to the head
# Initialize a fast pointer to the head
# Initialize an empty stack
# While fast and its next node both exist
# Push the value of slow onto the stack
# Advance the slow ptr
# Advance the fast twice
# If fast exists (the list is an odd length), advance the slow ptr
# While slow exists
# If slow's value is not equal to the top element in the stack, return false
# Advance the slow ptr
# It's a palindrome so return true



# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):
    slow = head
    fast = head
    stack  = []
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
        
    while slow:
        if slow.value != stack.pop():
            return False
        slow = slow.next
        
    return True