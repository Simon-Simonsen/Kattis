import sys
import heapq
from math import sqrt
from collections import deque

def load_island_data():
    data = deque(line.strip() for line in sys.stdin if line.strip())
    num_cases = int(data.popleft())
    cases = []

    for _ in range(num_cases):
        m = int(data.popleft())
        islands = []
        for _ in range(m):
            x, y = map(float, data.popleft().split())
            islands.append((x, y))
        cases.append(islands)
    
    return cases

def compute_distance(island1, island2):
    x1, y1 = island1
    x2, y2 = island2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Prim's Algorithm for Minimum Spanning Tree
def prim_mst(islands):
    m = len(islands)
    total_cost = 0.0
    min_heap = []
    in_mst = [False] * m
    min_edge = [(float('inf'), -1)] * m  # (cost, from_node)
    min_edge[0] = (0.0, -1)  # Start from island 0

    # Start by pushing the first island (0) into the heap
    heapq.heappush(min_heap, (0.0, 0))  # (cost, island_index)

    while min_heap:
        cost, island = heapq.heappop(min_heap)
        
        # If already in MST, continue
        if in_mst[island]:
            continue

        # Mark the current island as part of the MST
        in_mst[island] = True
        total_cost += cost

        # Update the neighboring islands' edges
        for neighbor in range(m):
            if not in_mst[neighbor]:
                distance = compute_distance(islands[island], islands[neighbor])
                if distance < min_edge[neighbor][0]:
                    min_edge[neighbor] = (distance, island)
                    heapq.heappush(min_heap, (distance, neighbor))

    return total_cost

if __name__ == "__main__":
    cases = load_island_data()
    for idx, islands in enumerate(cases):
        result = prim_mst(islands)
        print(f"{result}")
