import matplotlib.pyplot as plt
from math import comb

def disponibilidade_geral(n, k, p):
    disponibilidade = 0
    for i in range(k, n + 1):
        disponibilidade += comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return disponibilidade

def gerar_dados(n_values, p_values):
    dados = {}
    for n in n_values:
        k_values = [1, n, (n // 2) + 1]
        for k in k_values:
            key = (n, k)
            disponibilidades = []
            for p in p_values:
                disponibilidade = disponibilidade_geral(n, k, p)
                disponibilidades.append(disponibilidade)
            dados[key] = disponibilidades
    return dados

def plotar_graficos(dados, p_values, filename):
    plt.figure(figsize=(10, 6))
    
    for (n, k), disponibilidades in dados.items():
        plt.plot(p_values, disponibilidades, label=f'n={n}, k={k}')
    
    plt.xlabel('Probabilidade de Disponibilidade de Cada Servidor (p)')
    plt.ylabel('Disponibilidade do Serviço')
    plt.title('Disponibilidade vs Probabilidade para diferentes valores de n e k')
    plt.grid(True)
    plt.legend()
    
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    n_values = [3, 5, 7]
    p_values = [i / 10 for i in range(11)]
    
    dados = gerar_dados(n_values, p_values)
    
    plotar_graficos(dados, p_values, 'grafico.png')

    n = 2
    k = 1
    p = 0.69

    valor = disponibilidade_geral(n, k, p)
    print(f"\nDisponibilidade: {valor:.4f}")