

#define heuristic no. of incorrect position
#square matrix

def heuristic(start,goal):
    row = len(start[0])
    column = row
    count = 0
    for i in range(row):
        for j in range (column):
            if start[i][j] != goal[i][j] and start[i][j]!= 0:
                count +=1

    return count

def print_graph(state):
    for i in state:
        for j in i:
            print(j ,end = "   ")
        
        print("")

def neighbour(state,i,j):
    row = len(state[0])
    '''if i == row/2 and j == row/2:
        return [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
    elif i==0 and j == 0:
        return [(i+1,j),(i,j+1)]
    elif i==0 and j== row-1:
        return [(i,j-1),(i+1,j)]
    elif i = '''
    neighbours = []
    if i+1<row:
        neighbours.append((i+1,j))
    
    if j+1<row:
        neighbours.append((i,j+1))
    if i-1>= 0:
        neighbours.append((i-1,j))
    if j-1>= 0:
        neighbours.append((i,j-1))

    return neighbours

def Astar(start,goal):
    row = len(start[0])




graph = [
    [1,2,3],[7,8,4],[0,6,5]
]

goal =  [
    [1,2,3],[8,0,4],[7,6,5]
]

h = heuristic(graph,goal)
print(h)

nei = neighbour(graph,2,0)
print(nei)

print_graph(graph)
print("\n")
for n in nei:
    (x,y) = n
    gr =graph
    temp = gr[2][0]
    gr[2][0] = gr[x][y]
    gr[x][y] = temp

    print_graph(gr)
    print("\n\n\n")