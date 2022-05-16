def shortestPath(g, k):
    r, c = len(g), len(g[0])
    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    mem = set([(0, 0, k)])
    q = [(0, 0, k)]
    step = 0
    while q:
        n = len(q)
        for _ in range(n):
            x, y, pre = q.pop(0)  # 将当以前的点赋给（x，y，pre）来进行下一步。
            if x == r - 1 and y == c - 1:
                return step
            for i, j in d:  # 利用BFS找出每次移动后的所有点g[nx][ny]
                nx, ny = x + i, y + j
                if nx >= 0 and nx < r and ny >= 0 and ny < c:

                    # 规定条件确保所搜点再矩阵内部
                    if g[nx][ny] == 1:  # 当遇到障碍物时
                        if pre and (nx, ny, pre - 1) not in mem:
                            q.append((nx, ny, pre - 1))
                        mem.add((nx, ny, pre - 1))
                    else:
                        if (nx, ny, pre) not in mem:
                            q.append((nx, ny, pre))
                            mem.add((nx, ny, pre))
        step += 1
    return -1