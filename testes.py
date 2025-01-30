from simulador_epidemia import *
from time import sleep

# Definição do grafo
grafo1 = np.array([[0, 4, 10, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                        [10, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 5, 6],
                        [1, 0, 1, 0, 3, 2, 2, 1, 0, 0, 0, 0, 0],
                        [3, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 2, 0, 0, 0, 0, 9, 1, 5, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 9, 0, 3, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 8, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 5, 0, 8, 0, 7, 0],
                        [0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 7, 0, 8],
                        [0, 9, 6, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0]])

# Parâmetros da simulação
T = 150
coef_infeccao = 0.5
coef_recuperacao = 0.2

simular_propagacao(grafo1, coef_infeccao, coef_recuperacao, T)

sleep(2)

grafo2 = [[0, 5, 1, 0, 2, 3, 0],
          [5, 0, 0, 5, 1, 0, 0],
          [1, 0, 0, 0, 0, 1, 8],
          [0, 0, 5, 0, 0, 0, 0],
          [2, 1, 0, 0, 0, 0, 0],
          [3, 0, 1, 0, 0, 0, 0],
          [0, 0, 8, 0, 0, 0, 0]]

# Parâmetros da simulação
T = 150
coef_infeccao = 0.5
coef_recuperacao = 0.1

simular_propagacao(grafo2, coef_infeccao, coef_recuperacao, T)