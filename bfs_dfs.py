node_queue = []
node_stack = []
visited_bfs = []
visited_dfs = []

#BFS
def bfs(input_graph, node):
    visited_bfs.append(node)
    node_queue.append(node)
    #print(node)

    while(node_queue):
        n = node_queue.pop(0)
        print(n)

        for neighbour in input_graph[n]:
            if neighbour not in visited_bfs:
                visited_bfs.append(neighbour)
                node_queue.append(neighbour)


#DFS
def dfs(graph, node):
    visited_dfs.append(node)
    node_stack.append(node)
    #print(node)

    while(node_stack):
        n = node_stack.pop()
        print(n)

        for neighbour in graph[n]:
            if neighbour not in visited_dfs:
                visited_dfs.append(neighbour)
                node_stack.append(neighbour)


def main():
    input_graph = {
        '5':['3', '7'],
        '3': ['2', '4'],
        '7':['8'],
        '2':[],
        '4':[],
        '8':[],
        '10':['11'],
        '11':['12'],
        '12':[]
    }
    

    input_graph1 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
    }

    print("BFS of input graph")
    bfs(input_graph, '5')
    print("BFS of input graph1")
    bfs(input_graph1, 'A')
    
    print("DFS of input graph")
    dfs(input_graph, '5')
    print("DFS of input graph1")
    dfs(input_graph1, 'A')




if __name__=="__main__":
    main()
