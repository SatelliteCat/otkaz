
# Топология сети связи
graph = [
#    0,1,2,3,4,5,6,7,8,9
    [0,1,0,0,1,0,1,0,0,0], # 0
    [1,0,1,1,0,0,0,0,0,0], # 1
    [0,1,0,0,0,0,0,0,0,0], # 2
    [0,1,0,0,0,0,0,0,0,0], # 3
    [1,0,0,0,0,1,1,0,0,0], # 4
    [0,0,0,0,1,0,1,1,0,0], # 5
    [1,0,0,0,0,1,0,1,0,0], # 6
    [0,0,0,0,0,1,1,0,1,0], # 7
    [0,0,0,0,0,0,0,1,0,1], # 8
    [0,0,0,0,0,0,0,0,1,0]] # 9
print(graph)

# длин линий связи между узлами

# интенсивностей отказов узлов

# интенсивностей отказов линий связи между узлами

# интенсивностей восстановлений

# Закон распределения времен отказов элементов

# Закон распределения времен восстановлений элементов

# Номер начального и конечного узлов для поиска

# количество отказов в сети связи

# Дисциплина восстановления

cnt = 0 # количество путей
n = 10 # количество вершин
visited = [0,0,0,0,0,0,0,0,0,0] # отметки посещенных вершин
v = 1 # начальная вершина
x = 3 # конечная вершина
def finder(graph, visited, n, v, x, cnt):
    index = 0
    isEnd = False

    while (isEnd != True):
        # пропускаем, если узел является конечным
        if (v == x):
            index += 1
            isEnd = True
        
        visited[v] = True
        for i in range(0, n):
            if graph[v][i] and not visited[i]:
                finder(graph, visited, n, i, x, cnt)
        
        visited[v] = False

finder(graph, visited, n, v, x, cnt)
print(cnt)