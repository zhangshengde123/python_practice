
def show_spiral_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    row, col = 0, 0
    num, direction = 1, 0
    while num <= n**2:
        if matrix[row][col] == 0:
            matrix[row][col] = num
            num += 1
        if direction == 0:
            if col < n-1 and matrix[row][col+1] == 0:
                col += 1
            else:
                direction += 1
        elif direction == 1:
            if row < n-1 and matrix[row+1][col] == 0:
                row += 1
            else:
                direction += 1
        elif direction == 2:
            if col > 0 and matrix[row][col-1] == 0:
                col -= 1
            else:
                direction += 1
        elif direction == 3:
            if row > 0 and matrix[row-1][col] == 0:
                row -= 1
            else:
                direction += 1
        direction %= 4
    for x in matrix:
        for y in x:
            print(y, end='\t')
        print()


show_spiral_matrix(2)


# print([[0]*7 for _ in range(7)])