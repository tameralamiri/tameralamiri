## Linked Lists:
Linked lists are linear data structure, an alternative to arrays, but we can only access the values

* arrays are static because they must be defined contiguously in memory, while linked lists are dynamic because they only need enough memory to store the node data and a reference to the next node.
* arrays have a length, while linked lists only have a pointer to the beginning of the list called the head.




### Node Structure:
```python
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None
```

### Linked List:
```python

# Option 1:
node1 = ListNode(1)
node2 = ListNode(2)

node1.next = node2

# Option 2:
linkedlist = ListNode(1, ListNode(2))
```
### Nodes vs Values:
Node is a wrapper around its values, which means:
* you can only traverse a linked list using the node
* you can only applying operations on the node values

```python
head = ListNode(1, ListNode(2, ListNode(3)))
sum = 0 
curr = head
while curr:
    sum += curr.value
    curr = curr.next

```

### Working with Pointers:
```python
# curr: We use curr to point to current node, and it's useful when iterating over a linked list
head = ListNode(1, ListNode(2, ListNode(3)))
curr = head
while curr:
    curr = curr.next # this is equivelent to index + 1 when iterating over an array.
                     # note that curr.next = curr is completely different, and means pointing the curr Node to itself

# next: this point to the next node, it's helpful when we try to add new nodes in the middle of a list
head = ListNode(1, ListNode(2, ListNode(3))) # 1 -> 2 -> 3
node = ListNode(4) # if we want to add 4 to the list like this 1 -> 4 -> 2 -> 3

next = head.next # next points to 2 -> 3
head.next = node # 1 -> 4
node.next = next # 1 -> 4 -> 2 -> 3

# removing a node: to remove a node, we want the previous node to skip it and point to the next node
head = ListNode(1, ListNode(2, ListNode(3))) # 1->2->3
head.next = head.next.next # 1->3

# removing a node with a pointer to the node it self
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4)))) # 1->2->3->4
def delete_node(node):
    node.value = node.next.value
    node.next = node.next.next

# swapping a node: swap 1->2->3 to 2->1->3
head = ListNode(1, ListNode(2, ListNode(3)))
new_head = head.next # new_head 2 -> 3
head.next = head.next.next # 1->3
new_head.next = head # 2->1->3
```

## Double Linked Lists:
Similar to linked lists but each node points to the next and previous nodes, and instead of providing the head only, sometimes we are provided with `head` and `tail` to allow traversal from the beginning or end of the list.

### Double Linked List Node Structure:
```python
class DLLNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

dllhead = DLLNode(1)
node2 = DLLNode(2)
node3 = DLLNode(3)
dlltail = DLLNode(4)

dllhead.next = node2
node2.next = node3
node3.next = dlltail

dlltail.prev = node3
node3.prev = node2
node2.prev = dllhead
```

### Dummy Node (Sentinel Node):
the pattern of creating a dummy node is used to avoid special cases when dealing with the beginning or end of a linked list(single or double ones).

How to implement it:
1. create a dummy node to represent the head with a dummy value and point dummy.next to the real head
2. at the end of the function return dummy.next to send the real head

When to use it:
1. with operations on the list that might change the head (adding a new node, reordering)
2. In slow/fast pattern where the slow pointer need to be one node before the fast one (dummy.next = head, slow = dummy, fast = head)
3. Copying a list to a new one

```python
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
head = Node(2, Node(4, Node(6, Node(8))))

def copy_linked_list(head):
    dummy = Node(0)
    copy = dummy
    curr = head
    while curr:
        copy.next = Node(curr.value)
        copy = copy.next
        curr = curr.next
    return dummy.next

def print_ll(head):
    while head:
        print(str(head.value)+'->', end="")
        head = head.next
    print(None)

print_ll(copy_linked_list(head))
```


## Using two pointers in a linked list:
This technique can be used to solve common problems: detect cycles, finding middle elements, removing nth node from the end.

```python
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = None

def has_cycle(head: Node) -> bool:
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

def find_middle(head: Node) -> Node:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def remove_nth_from_end(head: Node, n: int) -> Node:
    dummy = Node(0)
    dummy.next = head

    first = dummy
    second = dummy

    for _ in range(n+1):
        first = first.next
    
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next
```

[More linked-lists examples in python](linkedlists.py)