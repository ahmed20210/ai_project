import heapq
import time
from collections import deque


GOAL = (0, 1, 2, 3, 4, 5, 6, 7, 8)


def print_state(state):
    """Pretty print a puzzle state."""
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(" ".join(str(x) if x != 0 else "·" for x in row))
    print()

def get_neighbors(state):
    """Get all valid neighbor states from current state."""
    neighbors = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        new_r, new_c = row + dr, col + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_zero = new_r * 3 + new_c
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
    
    return neighbors

def reconstruct_path(parent, start, goal):
    """Reconstruct path from start to goal using parent map."""
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)
    return path[::-1]

def is_solvable(state):
    """Check if puzzle is solvable using inversion count."""
    inversions = 0
    flat = [x for x in state if x != 0]
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    return inversions % 2 == 0

def manhattan_distance(state):
    """Calculate Manhattan distance heuristic."""
    distance = 0
    for i in range(1, 9):
        curr = state.index(i)
        goal = i
        distance += abs(curr // 3 - goal // 3) + abs(curr % 3 - goal % 3)
    return distance

def misplaced_tiles(state):
    """Calculate misplaced tiles heuristic."""
    return sum(1 for i in range(1, 9) if state[i] != i)

def bfs(start):
    """Breadth-First Search algorithm."""
    if start == GOAL:
        return 0, [start]
    
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    nodes = 0
    
    while queue:
        state = queue.popleft()
        nodes += 1
        
        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = state
                
                if next_state == GOAL:
                    path = reconstruct_path(parent, start, next_state)
                    return nodes, path
                
                queue.append(next_state)
    
    return nodes, []

def astar(start, heuristic_func):
    """A* Search algorithm."""
    if start == GOAL:
        return 0, [start]

    pq = []
    heapq.heappush(pq, (heuristic_func(start), 0, start))
    
    parent = {start: None}
    cost = {start: 0}
    visited = set()
    nodes = 0

    while pq:
        _, g, state = heapq.heappop(pq)
        nodes += 1

        if state == GOAL:
            path = reconstruct_path(parent, start, state)
            return nodes, path

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_neighbors(state):
            new_cost = g + 1
            if next_state not in cost or new_cost < cost[next_state]:
                cost[next_state] = new_cost
                priority = new_cost + heuristic_func(next_state)
                heapq.heappush(pq, (priority, new_cost, next_state))
                parent[next_state] = state

    return nodes, []
