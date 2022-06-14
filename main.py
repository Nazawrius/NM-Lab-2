from prohonka import method_prohonky
from zejdel import method_zejdelia

A = [[-4, 3, 0, 0], [2, 7, -3, 0], [0, -1, -5, -1], [0, 0, 2, 6]]
f = [4, 12, -9, 1]

x0 = [1, 2, 1, 0]
eps = 1e-2

# A = [[1, 1, 0], [1, 3, 2], [0, 1, 2]]
# f = [1, 1, 1]

# A = [[3, -1, 1], [-1, 2, 0.5], [1, 0.5, 3]]
# f = [1, 1.75, 2.5]
# x0 = [0, 0, 0]
# eps = 0.5

method_prohonky(A, f)

method_zejdelia(A, f, eps, x0)

