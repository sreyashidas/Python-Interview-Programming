def exist(board, word):
    solution = False
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False

def dfs(board, row, col, word):
    print 'dfs',board, row, col, word
    if len(word) == 0:
        return True

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[0]:
        return False

    temp = board[row][col]
    print 'temp', temp
    board[row][col] = ''
    result = dfs(board, row + 1, col, word[1:]) or dfs(board, row - 1, col, word[1:]) or dfs(board, row, col + 1,
                                                                                             word[1:]) or dfs(board,
                                                                                                              row,
                                                                                                              col - 1,
                                                                                                              word[1:])
    board[row][col] = temp

    return result

result = exist([['A','B','C','E'],['S', 'F', 'C', 'S'],['A', 'D', 'E', 'E']], 'ABCCED')
print result
