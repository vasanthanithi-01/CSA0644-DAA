def gameOfLife(board):
    rows = len(board)
    cols = len(board[0])

    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0),  (1,1)]

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            live = 0

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols:
                    live += board[ni][nj]

            if board[i][j] == 1 and (live == 2 or live == 3):
                result[i][j] = 1
            elif board[i][j] == 0 and live == 3:
                result[i][j] = 1

    return result

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))