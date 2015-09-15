class Queue:
    
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) is 0

queue = Queue()
queue.enqueue(1)
assert(queue.isEmpty() is False)
assert(queue.dequeue() is 1)
assert(queue.isEmpty() is True)


def doBreadthFirstSearch(graph, source):
    bfsInfo = []
    vertex = 0
    while vertex < len(graph):
        bfsInfo.append({"distance": None, "predecessor": None})
        vertex = vertex + 1

    queue = Queue()
    queue.enqueue(source)
    bfsInfo[source]["distance"] = 0

    while queue.isEmpty() is False:
        vertex = queue.dequeue()
        i = 0
        while i < len(graph[vertex]):
            neighbor = graph[vertex][i]
            if bfsInfo[neighbor]["distance"] is None:
                bfsInfo[neighbor]["distance"] = bfsInfo[vertex]["distance"] + 1
                bfsInfo[neighbor]["predecessor"] = vertex
                queue.enqueue(neighbor)

            i = i + 1

    return bfsInfo

adjacencyList = [
    [1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []
]
bfsInfo = doBreadthFirstSearch(adjacencyList, 3)
assert(bfsInfo[0] == {"distance": 4, "predecessor": 1});
assert(bfsInfo[1] == {"distance": 3, "predecessor": 4});
assert(bfsInfo[2] == {"distance": 1, "predecessor": 3});
assert(bfsInfo[3] == {"distance": 0, "predecessor": None});
assert(bfsInfo[4] == {"distance": 2, "predecessor": 2});
assert(bfsInfo[5] == {"distance": 2, "predecessor": 2});
assert(bfsInfo[6] == {"distance": 1, "predecessor": 3});
assert(bfsInfo[7] == {"distance": None, "predecessor": None});