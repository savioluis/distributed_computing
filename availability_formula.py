from math import comb

def disponibilidade_geral(n, k, p):
    disponibilidade = 0
    for i in range(k, n + 1):
        disponibilidade += comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return disponibilidade

n = 2
k = 1
p = 0.69

disponibilidade = disponibilidade_geral(n, k, p)
print(disponibilidade)