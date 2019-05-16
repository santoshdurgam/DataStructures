class Queue:
    def __init__(self):
        self.queue = []

    def addtoQ(self, value):
        self.queue.insert(0,value)
        return True

    def sprint(self):
        print(self.queue)

    def removefromQ(self):
        self.queue.pop()

q = Queue()
q.addtoQ(10)
q.addtoQ(20)
q.addtoQ(30)

q.sprint()
q.removefromQ()
q.sprint()
