node_queue = []
node_stack = []
visited_bfs = []
visited_dfs = []

#BFS
def bfs(input_graph, node):
    visited_bfs.append(node)
    node_queue.append(node)

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

    input_graph2 = {
    '0' : ['1','3'],
    '1' : ['2', '3', '5'],
    '2' : ['1', '3', '5'],
    '3' : ['0', '1', '2', '4'],
    '4' : ['2', '3', '6'],
    '5' : ['1', '2'],
    '6' : ['1', '4']
    }

    print("BFS of input graph")
    bfs(input_graph, '5')
    print("BFS of input graph1")
    bfs(input_graph1, 'A')
    visited_bfs.clear()
    
    print("DFS of input graph")
    dfs(input_graph, '5')
    print("DFS of input graph1")
    dfs(input_graph1, 'A')
    visited_dfs.clear()


    print("DFS of input graph2 mmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
    dfs(input_graph2, '0')
    visited_dfs.clear()


if __name__=="__main__":
    main()
