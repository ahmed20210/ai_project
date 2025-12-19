from solution import *

if __name__ == "__main__":
    start_state = (1, 0, 2,
                   3, 4, 5,
                   6, 7, 8)

    print("8-Puzzle Problem\n")
    print("Start State:")
    print_state(start_state)

    if not is_solvable(start_state):
        print("This puzzle is NOT solvable.")
        exit()

    # BFS
    t0 = time.time()
    bfs_nodes, bfs_path = bfs(start_state)
    t1 = time.time()

    print("--- BFS ---")
    print("Time:", round(t1 - t0, 5), "sec")
    print("Nodes Expanded:", bfs_nodes)
    print("Steps:", len(bfs_path) - 1)

    # A* with Manhattan
    t0 = time.time()
    astar_nodes, astar_path = astar(start_state, manhattan_distance)
    t1 = time.time()

    print("\n--- A* (Manhattan Distance) ---")
    print("Time:", round(t1 - t0, 5), "sec")
    print("Nodes Expanded:", astar_nodes)
    print("Steps:", len(astar_path) - 1)

    print("\nSolution Path (A*):")
    for state in astar_path:
        print_state(state)
