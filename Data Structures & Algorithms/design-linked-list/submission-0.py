class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        prev_node = self.left
        next_node = self.left.next
        
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        
    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0:
            new_node = ListNode(val)
            prev_node = curr.prev
            next_node = curr

            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = next_node
            next_node.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and curr != self.right and index == 0:
            prev_node = curr.prev
            next_node = curr.next
            prev_node.next = next_node
            next_node.prev = prev_node