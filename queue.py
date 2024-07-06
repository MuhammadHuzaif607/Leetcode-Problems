class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,el):
        self.queue.insert(0,el)

    def dequeue(self):
        print(self.queue.pop())

    def peek(self):
        print(self.queue[-1])

    def printqueue(self):
        print(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.peek()
q.printqueue()