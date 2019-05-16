class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class double_linked_list:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur=cur.next
            new_node.prev = cur
            cur.next = new_node
    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = node(data)
                nxt = cur.next
                new_node.next = nxt
                new_node.prev = cur
                cur.next = new_node
                nxt.prev = new_node
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.prepend(data)
            elif cur.data == key:
                new_node = node(data)
                prv = cur.prev
                new_node.next = cur
                new_node.prev = prv.prev
                prv.next = new_node
                cur.prev = new_node
            cur = cur.next

    def pop(self):
        if self.head is None:
            return -1
        else:
            cur = self.head
            self.head = cur.next
            cur.prev = None

    def delete(self, key):
        cur = self.head
        while cur:
            #if only one node
            if cur == self.head and cur.data == key:
                
            else:
                while

            cur = cur.next
    def print_list(self):
        cur = self.head
        while cur:
            print cur.data,
            cur = cur.next
        print "\n"

dll = double_linked_list()
dll.append(10)
dll.append(20)
dll.append(30)

dll.print_list()
dll.prepend(5)
dll.prepend(0)

dll.print_list()
dll.add_after_node(20, 25)
dll.print_list()

dll.add_after_node(30, 35)
dll.print_list()

dll.add_before_node(30, 29)
dll.print_list()

dll.pop()
dll.print_list()