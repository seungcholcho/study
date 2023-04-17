n = input().split()
N, M, V = int(n[0]), int(n[1]), int(n[2])
vertex_list = [i for i in range(N)]
edge = []
for i in range(0,M):
    a, b = map(int, input().split())
    a = a-1
    b = b-1
    temp = (a,b)
    edge.append(temp)
    temp = (b,a)
    edge.append(temp)

adj = [ [] for v in vertex_list]
print(adj)
for e in edge:
    adj[e[0]].append(e[1])
print(adj)

def stack_graph(adjac_lst):
    stack = [V-1]
    visit_vert = []
    while stack:
        current = stack.pop()
        for neighbor in adjac_lst[current]:
            if neighbor not in visit_vert:
                stack.append(neighbor)
        visit_vert.append(current)
    return visit_vert

visited = [i+1 for i in stack_graph(adj)]
print(visited)