import heapq

# CHANGE THIS TO YOUR OWN FILE PATH IF NEEDED
INPUT_FILE = r"D:\algorithms\AI Lab Report\input.txt"

def read_input():
    with open(INPUT_FILE, "r") as f:
        R, C = map(int, f.readline().split())
        grid = []
        for _ in range(R):
            grid.append(list(map(int, f.readline().split())))
        sr, sc = map(int, f.readline().split())
        tr, tc = map(int, f.readline().split())
    return R, C, grid, (sr, sc), (tr, tc)

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(R, C, grid, start, target):
    (sr, sc) = start
    (tr, tc) = target
    
    # If the start or target is blocked
    if grid[sr][sc] == 1 or grid[tr][tc] == 1:
        return None
    
    open_set = []
    heapq.heappush(open_set, (0, sr, sc))
    
    g_cost = {start: 0}
    parent = {start: None}
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while open_set:
        _, r, c = heapq.heappop(open_set)
        
        if (r, c) == target:
            path = []
            cur = target
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return path[::-1]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                new_cost = g_cost[(r, c)] + 1
                
                if (nr, nc) not in g_cost or new_cost < g_cost[(nr, nc)]:
                    g_cost[(nr, nc)] = new_cost
                    f_cost = new_cost + manhattan((nr, nc), target)
                    heapq.heappush(open_set, (f_cost, nr, nc))
                    parent[(nr, nc)] = (r, c)
    
    return None

def main():
    R, C, grid, start, target = read_input()
    path = a_star(R, C, grid, start, target)
    
    if path is None:
        print("Path not found using A*")
    else:
        print(f"Path found with cost {len(path)-1} using A*")
        print("Shortest Path:", path)

if __name__ == "__main__":
    main()
