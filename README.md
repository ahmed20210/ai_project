# 8-Puzzle Solver

This project implements an 8-puzzle solver using Breadth-First Search (BFS) and A* Search algorithms in Python.

## Description

The 8-puzzle is a sliding puzzle that consists of a frame of numbered square tiles in random order with one tile missing. The object of the puzzle is to place the tiles in order by making sliding moves that use the empty space.

This solver allows you to define a start state and finds the solution path to the goal state:
```
0 1 2
3 4 5
6 7 8
```
(where 0 represents the empty space)

## Features

- **Breadth-First Search (BFS)**: Explores all neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. Guarantees the shortest path.
- **A* Search**: Uses a heuristic function (Manhattan Distance) to guide the search. efficient and guarantees the shortest path if the heuristic is admissible.
- **Solvability Check**: Determines if the given initial state is solvable before attempting to solve it.

## Prerequisites

- Python 3.x

## Usage

1.  Clone the repository:
    ```bash
    git clone https://github.com/ahmed20210/ai_project.git
    cd ai_project
    ```

2.  Run the main script:
    ```bash
    python3 main.py
    ```

## Example Output

```text
8-Puzzle Problem

Start State:
1 · 2
3 4 5
6 7 8

--- BFS ---
Time: 0.00035 sec
Nodes Expanded: 1
Steps: 1

--- A* (Manhattan Distance) ---
Time: 0.00012 sec
Nodes Expanded: 2
Steps: 1

Solution Path (A*):
1 · 2
3 4 5
6 7 8

· 1 2
3 4 5
6 7 8
```

## files
- `main.py`: The entry point of the application.
- `solution.py`: Contains the implementation of the search algorithms and helper functions.
