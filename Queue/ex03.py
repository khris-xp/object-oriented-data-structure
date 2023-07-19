class Queue:
    def __init__(self):
        self.queue = []
        self.error_input = 0
        self.dequeue_count = 0
        self.queue_start = 0

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)
    
    def __len__(self):
        return self.size()

queue = Queue()

inp = input("input : ").split(',')

for i in inp:
    print("Step : " + i)
    if (i[0] == 'D'):
        if(queue.is_empty()):
            queue.dequeue_count += int(i[1:])
        elif(queue.size() > 0):
            queue.dequeue_count += (int(i[1:]) - queue.size())
        for j in range(int(i[1:])):
            queue.dequeue()
        print("Dequeue :", queue.queue)
        print("Error Dequeue : " + str(queue.dequeue_count))
        print("Error input :", queue.error_input)
        print('--------------------')
    elif (i[0] == 'E' and int(i[1:]) != 0):
        for k in range(int(i[1:])):
            queue.enqueue('*' + str(k + queue.queue_start))
        queue.queue_start += int(k + 1)
        print("Enqueue :", queue.queue)
        print("Error Dequeue : " + str(queue.dequeue_count))
        print("Error input :", queue.error_input)
        print('--------------------')
    elif (i[0] == 'E' and int(i[1:]) == 0):
        print("Enqueue :", queue.queue)
        print("Error Dequeue : " + str(queue.dequeue_count))
        print("Error input :", queue.error_input)
        print('--------------------')
    else:
        queue.error_input += 1
        print(queue.queue)
        print("Error Dequeue : " + str(queue.dequeue_count))
        print("Error input :", queue.error_input)
        print('--------------------')