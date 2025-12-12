def read_input():
    # Read all input from input.txt
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    idx = 0

    R, C = map(int, lines[idx].split())
    idx += 1

    grid = []
    for _ in range(R):
        grid.append(list(map(int, lines[idx].split())))
        idx += 1

    _, sr, sc = lines[idx].replace(":", "").split()
    sr, sc = int(sr), int(sc)
    idx += 1

    _, tr, tc = lines[idx].replace(":", "").split()
    tr, tc = int(tr), int(tc)

    return R, C, grid, (sr, sc), (tr, tc)


def dls(r, c, target, grid, R, C, depth, limit, visited, path):
    if depth > limit:
        return False

    visited.add((r, c))
    path.append((r, c))

    if (r, c) == target:
        return True

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
            if (nr, nc) not in visited:
                if dls(nr, nc, target, grid, R, C, depth + 1, limit, visited, path):
                    return True

    path.pop()
    visited.remove((r, c))
    return False


def iddfs(R, C, grid, start, target):
    max_depth = R * C  

    for limit in range(max_depth + 1):
        visited = set()
        path = []
        if dls(start[0], start[1], target, grid, R, C, 0, limit, visited, path):
            return True, limit, path

    return False, max_depth, []


def main():
    R, C, grid, start, target = read_input()
    found, depth, path = iddfs(R, C, grid, start, target)

    if found:
        print(f"Path found at depth {depth} using IDDFS")
        print("Traversal Order:", path)
    else:
        print(f"Path not found at max depth {depth} using IDDFS")


if __name__ == "__main__":
    main()
