def stack_def(graph,startnode):
    need_visited, visited = list(),list()
    need_visited.append(startnode)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(stack_def(graph,'A'))

