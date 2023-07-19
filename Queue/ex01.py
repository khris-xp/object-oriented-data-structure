class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0

inp = input("Enter Input : ").split(",")
queue = Queue()

for i in inp:
    if i[0] == "E":
        queue.enqueue(i[2:])
        print("Add", i[2:], "index is", queue.queue.index(i[2:]))
    elif i[0] == "D":
        if not queue.is_empty():
            print("Pop", queue.dequeue(), "size in queue is", len(queue.queue))
        else:
            print(-1)

if queue.is_empty():
    print("Empty")
else:
    print("Number in Queue is : ", queue.queue)