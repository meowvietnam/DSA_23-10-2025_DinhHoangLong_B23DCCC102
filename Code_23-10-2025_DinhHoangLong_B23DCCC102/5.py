def solution(board):
    N = len(board)
    row_avg = [sum(board[i]) // N for i in range(N)]
    col_avg = [sum(board[j][i] for j in range(N)) // N for i in range(N)]
    diag1 = sum(board[i][i] for i in range(N)) // N
    diag2 = sum(board[i][N - 1 - i] for i in range(N)) // N
    all_avg = row_avg + col_avg + [diag1, diag2]
    return max(all_avg) + min(all_avg)

print(solution([[25,11,82,61,34],
                [87,98,91,76,95],
                [44,2,39,57,65],
                [69,32,51,16,41],
                [94,27,74,37,9]]))