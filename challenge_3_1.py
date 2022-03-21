# Challenge 3.1
def solution(map):

    mRow = len(map)
    mCol = len(map[0])

    dRow = [-1, 0, 1, 0]
    dCol = [0, 1, 0, -1]

    pathx = mRow-1
    pathy = mCol-1

    new_map = map

    count = 0

    path_length = []

    def count_path(parent, pathx, pathy, count):

        target = parent[pathx][pathy]
        if target != None:
            x = target[0]
            y = target[1]
            count += 1
            count_path(parent, x, y, count)
        else:
            count += 1
            path_length.append(count)

    def is_valid(map, visited, row, col):
        if (row >= 0 and col >= 0) and (row < mRow and col < mCol):
            if visited[row][col] == False:
                if (map[row][col] == 0):
                    return True
        return False

    def bfs(map, mRow, mCol):
        queue = []

        visited = [[False for i in range(mRow)] for j in range(mCol)]
        parent = [["" for i in range(mRow)] for j in range(mCol)]

        queue.append((0, 0))
        visited[0][0] = True

        parent[0][0] = None

        while queue:
            cell = queue.pop(0)
            x = cell[0]
            y = cell[1]

            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                if (is_valid(map, visited, adjx, adjy)):
                    queue.append((adjx, adjy))
                    visited[adjx][adjy] = True
                    parent[adjx][adjy] = cell
        count_path(parent, pathx, pathy, count)


    for i in range(mRow):
        for j in range(mCol):
            if map[i][j] == 1:
                new_map[i][j] = 0
                bfs(new_map, mRow, mCol)
                new_map[i][j] = 1

    return min(path_length)