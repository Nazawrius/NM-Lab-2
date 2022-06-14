def method_prohonky(A, f):
    def a(n):
        return A[n][n-1]
    
    def b(n):
        return A[n][n+1]
    
    def c(n):
        return -A[n][n]
    
    alpha = [None]
    beta = [None]
    z = [None]
    n = len(f)
    x = [0 for i in range(n)]

    alpha.append(b(0)/c(0))
    print(f'alpha1 = {alpha[1]}')

    beta.append(-f[0]/c(0))
    print(f'beta1 = {beta[1]}')

    for i in range(1, n - 1):
        z.append(c(i)-alpha[i]*a(i))
        print(f'z{i} = {z[i]}')

        alpha.append(b(i)/z[i])
        print(f'alpha{i+1} = {alpha[i+1]}')

        beta.append((-f[i]+a(i)*beta[i])/z[i])
        print(f'beta{i+1} = {beta[i+1]}')
    
    z.append(c(n - 1)-alpha[n - 1]*a(n - 1))
    print(f'z{n - 1} = {z[n - 1]}')
    
    x[n - 1] = (-f[n - 1] + a(n - 1)*beta[n - 1]) / z[n - 1]
    print(f'x{n} = {x[n - 1]}')

    for i in range(n - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
        print(f'x{i + 1} = {x[i]}')
