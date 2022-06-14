def method_zejdelia(A, b, eps, x0):
    def norm(k):
        if k == 0:
            return True
        
        return max(abs(x[j][k] - x[j][k - 1]) for j in range(n))

    n = len(b)
    x = [[x0[i]] for i in range(n)]
    print('X0 = (', end = '')
    for i in range(n - 1):
        print(f'{x[i][0]}, ', end='')
    print(f'{x[n - 1][0]})')
    k = 0

    while norm(k) > eps:
        for i in range(n):
            left_sum = -sum(A[i][j]/A[i][i]*x[j][k + 1] for j in range(0, i))
            right_sum = -sum(A[i][j]/A[i][i]*x[j][k] for j in range(i + 1, n))

            x[i].append(left_sum + right_sum + b[i]/A[i][i])

        k += 1
        print(f'X{k} = (', end = '')
        for i in range(n - 1):
            print(f'{x[i][k]}, ', end='')
        print(f'{x[n - 1][k]})')
