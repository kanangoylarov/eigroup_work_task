def generate_spiral_matrix(N):
    matrix = [[0] * N for _ in range(N)]
    num = 1
    if N % 2 == 1:
        x, y = N // 2, N // 2
    else:
        x, y = N // 2 - 1, N // 2 - 1

    matrix[x][y] = num
    num += 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    step = 1
    dir_idx = 0

    while num <= N * N:
        for _ in range(2):
            for _ in range(step):
                x += directions[dir_idx][0]
                y += directions[dir_idx][1]
                if 0 <= x < N and 0 <= y < N:
                    matrix[x][y] = num
                    num += 1
            dir_idx = (dir_idx + 1) % 4
        step += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))

def sum_diagonals(matrix):
    N = len(matrix)
    primary_sum = 0
    secondary_sum = 0

    for i in range(N):
        primary_sum += matrix[i][i]           
        secondary_sum += matrix[i][N - 1 - i] 


    return primary_sum,secondary_sum


N =int(input("Enter the size of the matrix: "))  
spiral_matrix = generate_spiral_matrix(N)
print_matrix(spiral_matrix)


primary_sum, secondary_sum = sum_diagonals(spiral_matrix)
print("Sum of both diagonals seperately are:", primary_sum, secondary_sum)
