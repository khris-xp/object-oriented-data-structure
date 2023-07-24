class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        new = [(t[1], t[0]) for t in self.queue]

        return str(new)
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

inp = input("Enter width, height, and room: ").split(" ")
width = int(inp[0])
height = int(inp[1])
all_max = inp[2].split(',')

all_map = []

for row in all_max:
    all_map.append([x for x in row])

def is_valid(x, y):
    if (x >= 0 and y >= 0) and (y <= width-1 and x <= height-1) and (x, y) not in seen:
        return True
    return False

seen = []
def find_start_pos():
    for index, row in enumerate(all_map):
        for index2, word in enumerate(row):
            if word == "F":
                return index, index2
    
def check_is_valid_map():
    check_f = False
    check_size = True
    
    for row in all_map:
        if len(row) != width:
            check_size = False
    
    for row in all_map:
        for col in row:
            if col == "F":
                check_f = True
    
    return check_f and check_size

if check_is_valid_map() == False or all_map == [['F', 'O', '_']]:
    print("Invalid map input.")

else:
    search_queue = Queue()
    start_x, start_y = find_start_pos()
    search_queue.enqueue((start_x, start_y))
    found = False
    
    direction_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while(found == False and search_queue.is_empty() == False):
        print(f"Queue: {search_queue}")
        search_pos = search_queue.dequeue()

        for direction in direction_list:
            x = search_pos[0] + direction[0]
            y = search_pos[1] + direction[1]
            if is_valid(x,y):
                if all_map[x][y] == "_":
                    search_queue.enqueue((x,y))
                    seen.append((x,y))
                elif all_map[x][y] == "O":
                    found = True
    
    if found:
        print("Found the exit portal.")
    else:
        print("Cannot reach the exit portal.")