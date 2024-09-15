import matplotlib.pyplot as plt
from itertools import product

def gerar_tabela_verdade(n):
    return list(product([0, 1], repeat=n))

def calcular_valores(tabela, p):
    valores = []
    for linha in tabela:
        probabilidade = 1
        for bit in linha:
            probabilidade *= (1 - p) if bit == 1 else p
        valores.append(probabilidade)
    return valores

def somar_resultados_sem_k_ou_mais_disponiveis(tabela, resultados, k):
    soma = 0
    for linha, resultado in zip(tabela, resultados):
        servidores_disponiveis = linha.count(1)
        if servidores_disponiveis <= k:
            soma += resultado
    return soma

def calcular_disponibilidade(n, p, k):
    tabela = gerar_tabela_verdade(n)
    resultados = calcular_valores(tabela, p)
    soma = somar_resultados_sem_k_ou_mais_disponiveis(tabela, resultados, k)

    return soma

def gerar_dados_para_grafico(n_values, k_values, p_values):
    resultados = {}
    for n in n_values:
        for k in k_values:
            key = (n, k)
            resultados[key] = []
            for p in p_values:
                disponibilidade = calcular_disponibilidade(n, p, k)
                resultados[key].append(disponibilidade)
    return resultados

def plotar_dados(dados, p_values):
    plt.figure(figsize=(12, 8))
    for (n, k), disponibilidades in dados.items():
        plt.plot(p_values, disponibilidades, label=f'n={n}, k={k}')
    
    plt.xlabel('Probabilidade de Disponibilidade de Cada Servidor (p)')
    plt.ylabel('Disponibilidade do Serviço')
    plt.title('Disponibilidade do Serviço vs Probabilidade')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    n_values = [3, 5, 7]
    k_values = [1, 5, 4]
    p_values = [i/10 for i in range(11)]

    dados = gerar_dados_para_grafico(n_values, k_values, p_values)
    plotar_dados(dados, p_values)

    n = 2
    p = 0.69
    k = 1

    valor = calcular_disponibilidade(n, p, k)
    print(f"\nDisponibilidade: {valor:.4f}")
