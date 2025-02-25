import heapq

def bfs(maze):
    start = maze.start
    goal = maze.goal
    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor in maze.get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

def dfs(maze):
    start = maze.start
    goal = maze.goal
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor in maze.get_neighbors(current):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None

def a_star(maze, heuristic):
    start = maze.start
    goal = maze.goal
    open_list = []
    heapq.heappush(open_list, (0, start, [start]))
    g_scores = {start: 0}
    visited = set()

    while open_list:
        _, current, path = heapq.heappop(open_list)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor in maze.get_neighbors(current):
            tentative_g = g_scores[current] + 1
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor, path + [neighbor]))

    return None

def greedy(maze, heuristic):
    start = maze.start
    goal = maze.goal
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start, [start]))
    visited = set()

    while open_list:
        _, current, path = heapq.heappop(open_list)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor in maze.get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor, path + [neighbor]))

    return None
