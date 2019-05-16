class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def appendList(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def printList(self):
        curr = self.head
        while curr:
            print curr.data,
            curr = curr.next

    def mergesort(self, head):
        if head is None or head.next is None:
            return head
        l1, l2 = self.divideLists(head)
        l1 = self.mergesort(l1)
        l2 = self.mergesort(l2)
        head = self.mergelists(l1, l2)
        return head

    def mergelists(self, l1, l2):
        temp = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.data <= l2.data:
            temp = l1
            temp.next = self.mergelists(l1.next, l2)
        else:
            temp = l2
            temp.next = self.mergelists(l1, l2.next)
        return temp

    def divideLists(self, head):
        slow = head
        fast = head

        if fast:
            fast = fast.next
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        mid = slow.next
        slow.next = None
        return head, mid

ll = LinkedList()
ll.appendList(40)
ll.appendList(20)
ll.appendList(0)
ll.appendList(56)
ll.appendList(10)

ll.printList()
print ""
ll.head = ll.mergesort(ll.head)
ll.printList()
