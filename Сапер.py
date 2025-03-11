import sys


def main():

    s = input()
    n, m, k = map(int, s.split())
    matrix = [[int(0) for i in range(m)] for j in range(n)]
  
    for j in range(k):
        b = input()
        o = list(map(int, b.split()))
        matrix[o[0] - 1][o[1] - 1] = '*'
        update_field(o[0] - 1, o[1] - 1, matrix)
    
    for i in range(n):
        print(*matrix[i][:])
    pass

def update_field(nn, mm, matrix):
    coords = [
        (nn - 1, mm),
        (nn - 1, mm - 1),
        (nn + 1, mm),
        (nn + 1, mm + 1),
        (nn, mm + 1),
        (nn, mm - 1),
        (nn + 1, mm - 1),
        (nn - 1, mm + 1)
    ]
    for i, j in coords:
        if i < 0 or j < 0 or i > (len(matrix) - 1) or j > (len(matrix[0][:]) - 1):
            continue
        if matrix[i][j] == '*':
            continue
        matrix[i][j] += 1


if __name__ == '__main__':
    main()