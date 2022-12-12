# Function for finding shortest path between nodes
# modified from: https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    #print("Shortest path = ", *new_path)
                    #print(f"path lenght: {len(new_path)-1}")
                    return len(new_path)-1
            explored.append(node)

    # Condition when the nodes
    # are not connected
    # return -1 if failed
    return -1

myFile = open("input_12_1.txt", "r")
#myFile = open("demoinput12.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")

map = []

for x in rsDataList:
    map.append(list(x))

start = [0,0]
end = [0,0]

startList = []

# find start, find end, find lowest points for part 2
for i, x in enumerate(map):
    for j, y in enumerate(x):
        if y == "S":
            start = [i,j]
            map[i][j] ="a"
            startList.append(f"{i},{j}")
        elif y == "E":
            end = [i,j]
            map[i][j] ="z"
        elif y == "a":
            startList.append(f"{i},{j}")

# create graph
tree = {}
for i, x in enumerate(map):
    for j, y in enumerate(x):
        tList = []
        # right
        if (j < len(x)-1) and (ord(map[i][j])+1) >= ord(map[i][j+1]):
            tList.append(f"{i},{j+1}")
        # left
        if (j > 0) and (ord(map[i][j])+1) >= ord(map[i][j-1]):
            tList.append(f"{i},{j-1}")
        # top
        if (i > 0) and (ord(map[i][j])+1) >= ord(map[i-1][j]):
            tList.append(f"{i-1},{j}")
        # bottom
        if (i < len(map)-1) and (ord(map[i][j])+1) >= ord(map[i+1][j]):
            tList.append(f"{i+1},{j}")
        # append node
        tree[f"{i},{j}"] = tList


# Do BFS for part 1
p1r = BFS_SP(tree, f"{start[0]},{start[1]}", f"{end[0]},{end[1]}")
print(f"Part 1 result: {p1r}")

# Dirty solution for part 2
# Starting value can be solution from part 1
p2r = p1r
# run BFS for possible starting point
for x in startList:
    tmp = BFS_SP(tree, x, f"{end[0]},{end[1]}")
    if tmp < p2r and tmp > 0:
        p2r = tmp

print(f"Part 2 result: {p2r}")