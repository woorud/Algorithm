def dfs(graph, start_node):
    visited = list()
    need_visit = list() # stack 생성

    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'G', 'H', 'I'],
    'D' : ['B', 'E', 'F'],
    'E' : ['D'],
    'F' : ['D'],
    'G' : ['C'],
    'H' : ['C'],
    'I' : ['C', 'J'],
    'J' : ['I']
    }

print(dfs(graph, 'A'))