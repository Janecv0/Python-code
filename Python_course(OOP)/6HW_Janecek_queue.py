class Queue:
    def __init__(self, maxsize:int):

        if maxsize <= 0:
            raise Warning("Maximum size can't be zero or smaller!")

        self.head = None
        self.tail = None
        self.maxsize = maxsize

    def empty(self):
        # is queue empty?
        if self.head == None:  # if there's no head, queue is empty
            return True
        else:
            return False

    def size(self):
        # what is the size of a queue? Baby don't hurt me...
        size = 0
        head = self.head
        while head is not None:  # if head exists, size++
            size += 1
            head = head.next
        return size

    def full(self):
        # is queue full?
        if self.size() == self.maxsize:  # queue is full
            return True
        elif self.size() > self.maxsize:  # something's wrong
            raise Warning("Queue is bigger than maxsize.")
        else:  # queue is not full
            return False
        pass

    def put(self, data):
        # put data in a queue
        new_node = Node(data)

        if self.empty():  # first in
            self.head = new_node  # new_node is new head and tail
            self.tail = new_node
            self.head.next = None  # can't have neighbors
            self.head.previous = None

        elif self.full():
            print("You can't add another node, queue is already full")


        else:
            last_node = self.head

            while last_node.next: #find last node
                last_node = last_node.next

            last_node.next = new_node #new_node is last

    def get(self):
        # get data from a queue
        if self.size() > 0: #check if there is anything to get
            self.head = self.head.next
            return self.tail.data
        else:
            print("Your list is empty!")
            return False

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(None)
        return f"{nodes}"


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

        ########testing##########


# queueueueue initialization
q = Queue(10)

# testing fullness and emptiness of empty queue
assert q.empty()
assert q.full() == False

# testing data insertion and emptiness
q.put("data1")
assert q.empty() == False

# testing data
data = ["data2", "data3", "data4", "data5", "data6", "data7", "data8", "data9"]
for i in range(len(data)):
    q.put(data[i])

assert q.full() == False
q.put("data10")
assert q.full()

# testing get
assert q.get() == "data1"
assert q.full() == False
assert q.size() == 9

for i in range(q.size()):
    q.get()

assert q.empty()

