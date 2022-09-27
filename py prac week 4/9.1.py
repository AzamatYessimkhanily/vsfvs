MAX = 100


def largestSquare(matrix, R, C, q_i, q_j, K, Q):
    for q in range(Q):
        i = q_i[q]
        j = q_j[q]
        min_dist = min(min(i, j),
                       min(R - i - 1, C - j - 1))
        ans = -1
        for k in range(min_dist + 1):

            count = 0

            for row in range(i - k, i + k + 1):
                for col in range(j - k, j + k + 1):
                    count += matrix[row][col]

            if count > K:
                break

            ans = 2 * k + 1
        print(ans)


matrix = [[1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 0, 1, 0]]
K = 9
Q = 1
q_i = [1]
q_j = [2]
largestSquare(matrix, 4, 5, q_i, q_j, K, Q)