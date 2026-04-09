# ==========================
# Drone Delivery Navigation
# ==========================

import heapq
from collections import deque

# --------- Graph Definition ---------
graph = {
    'A': {'B': 2, 'C': 5, 'D': 1},
    'B': {'A': 2, 'D': 2, 'E': 3},
    'C': {'A': 5, 'D': 2, 'F': 3},
    'D': {'A': 1, 'B': 2, 'C': 2, 'E': 1, 'F': 4},
    'E': {'B': 3, 'D': 1, 'G': 2},
    'F': {'C': 3, 'D': 4, 'G': 1},
    'G': {'E': 2, 'F': 1, 'H': 3},
    'H': {'G': 3}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 6,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 1,
    'H': 0
}

start = 'A'
goal = 'H'

# ===================================
# Depth-First Search (DFS)
# ===================================
def dfs(graph, start, goal):
    visited = set()
    path = []

    def dfs_helper(the_node):
        if the_node in visited:
            return False
        visited.add(the_node)
        path.append(the_node)
        
        if the_node == goal:
            return True
        
        for neighbouring_node in graph[the_node]:
            if dfs_helper(neighbouring_node):
                return True
            
        path.pop()
        return False
        # TODO: implement DFS recursion
        pass

    dfs_helper(start)
    return path

# ===================================
# Breadth-First Search (BFS)
# ===================================
def bfs(graph, start, goal):
    visited = set()
    queue = deque()
    queue.append((start, [start]))
    visited.add(start)
    
    while queue:
        present_node, path = queue.popleft()
        
        if present_node == goal:
            return path
        
        for neighbouring_node in graph[present_node]:
            if neighbouring_node not in visited:
                visited.add(neighbouring_node)
                queue.append((neighbouring_node, path + [neighbouring_node]))
                
    return []
    # TODO: implement BFS logic
    #pass

# ===================================
# Uniform Cost Search (UCS)
# ===================================
def ucs(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start, [start]))
    explored = set()
    
    while frontier:
        path_cost, the_node, path = heapq.heappop(frontier)
        
        if the_node in explored:
            continue
        
        explored.add(the_node)
        
        if the_node == goal:
            return path, path_cost
        
        for neighbouring_node, weight in graph[the_node].items():
            heapq.heappush(frontier, (path_cost + weight, neighbouring_node, path + [neighbouring_node]))
            
    return [], float('inf')
    # TODO: implement UCS logic
    #pass

# ===================================
# A* Search
# ===================================
def a_star(graph, start, goal, heuristic):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], 0, start, [start]))
    explored = set()
    
    while frontier:
        t_cost, path_cost, the_node, path = heapq.heappop(frontier)
        
        if the_node in explored:
            continue
        
        explored.add(the_node)
        if the_node == goal:
            return path, path_cost
        
        for neighbouring_node, weight in graph[the_node].items():
            new_path_cost = path_cost + weight
            new_t_cost = new_path_cost + heuristic[neighbouring_node]
            heapq.heappush(frontier, (new_t_cost, new_path_cost, neighbouring_node, path  + [neighbouring_node]))
            
    return [], float('inf')
    # TODO: implement A* logic
    #pass

# ===================================
# Run and Compare
# ===================================
if __name__ == "__main__":
    print("DFS Path:", dfs(graph, start, goal))
    print("BFS Path:", bfs(graph, start, goal))
    print("UCS Path:", ucs(graph, start, goal))
    print("A* Path:", a_star(graph, start, goal, heuristic))