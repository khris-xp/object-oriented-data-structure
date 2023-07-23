class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
    def is_full(self):
        return len(self.queue) == 5
    
inp = input("Enter people : ")

queue = Queue()

for i in inp:
    queue.enqueue(i)

cashier1_time = 0
cashier2_time = 0

cashier1 = Queue()
cashier2 = Queue()

for count in range(queue.size()):
    if not cashier1.is_empty():
        if cashier1_time == 2:
            cashier1.dequeue()
            cashier1_time = 0
        else:
            cashier1_time += 1
    if not cashier2.is_empty():
        if cashier2_time == 1:
            cashier2.dequeue()
            cashier2_time = 0
        else:
            cashier2_time += 1

    if not queue.is_empty() and not cashier1.is_full():
        cashier1.enqueue(queue.dequeue())
    elif not queue.is_empty() and not cashier2.is_full():
        cashier2.enqueue(queue.dequeue())
    
    print(f"{count+1} {queue.queue} {cashier1.queue} {cashier2.queue}")
