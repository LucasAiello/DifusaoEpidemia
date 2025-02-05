import matplotlib.pyplot as plt
import networkx as nx
from random import randrange
import numpy as np
from math import floor, ceil

def simular_propagacao(m_adj_grafo, coef_i, coef_r , tempo):

      infectados = []
      sucetiveis = []
      recuperados = []
      populacao_total = 0
      for  i in range(len(m_adj_grafo)):
        infectados.append(0)
        populacao = randrange(50, 300)
        populacao_total += populacao
        sucetiveis.append(populacao)
        recuperados.append(0)

      cidade_inicial = randrange(0, len(m_adj_grafo))
      infectados[cidade_inicial] = 1

      print(f"Cidade com primeiro infectado: {cidade_inicial}")

      # Armazenamento de dados para gráfico
      historico_s = [[] for _ in range(len(m_adj_grafo) + 1)]
      historico_i = [[] for _ in range(len(m_adj_grafo) + 1)]
      historico_r = [[] for _ in range(len(m_adj_grafo) + 1)]

      for i in range(tempo):
        populacao_total = 0
        for k in range(len(infectados)):
            populacao_total += infectados[k] + sucetiveis[k] + recuperados[k]

        soma_s = 0
        soma_i = 0
        soma_r = 0

        for c in range(len(infectados)):

            if populacao_total > 0:
              novos_infectados = ceil(coef_i * ((sucetiveis[c] * infectados[c])/(sucetiveis[c] + infectados[c] + recuperados[c])))
            else:
              novos_infectados = 0


            novos_recuperados = floor(coef_r * infectados[c])

            infectados[c] += novos_infectados - novos_recuperados
            sucetiveis[c] -= novos_infectados

            recuperados[c] += novos_recuperados

            historico_s[c].append(sucetiveis[c])
            soma_s += sucetiveis[c]

            historico_i[c].append(infectados[c])
            soma_i += infectados[c]

            historico_r[c].append(recuperados[c])
            soma_r += recuperados[c];


        historico_s[-1].append(soma_s)
        historico_i[-1].append(soma_i)
        historico_r[-1].append(soma_r)

        for i in range(len(infectados)):
            for j in range(len(infectados)):

                if m_adj_grafo[i][j] > 0:

                    if infectados[i] != 0:

                        prob = randrange(0, 3)

                        if prob == 1:
                            nova_populacao = randrange(0, floor(infectados[i]) + 1)
                            nova_populacao %= m_adj_grafo[i][j] + 1

                            infectados[i] -= nova_populacao
                            infectados[j] += nova_populacao

                        elif prob == 2:
                            nova_populacao = randrange(0, floor(sucetiveis[i]) + 1)
                            nova_populacao %= m_adj_grafo[i][j] + 1

                            sucetiveis[i] -= nova_populacao
                            sucetiveis[j] += nova_populacao
                        else:
                          nova_populacao = randrange(0, floor(recuperados[i]) + 1)
                          nova_populacao %= m_adj_grafo[i][j] + 1

                          recuperados[i] -= nova_populacao
                          recuperados[j] += nova_populacao


      # Determinar nó mais influente
      valores, vetores = np.linalg.eig(m_adj_grafo)
      indice_mais_influente = np.argmax(np.abs(vetores[:, np.argmax(np.abs(valores))]))

      def plotar_graficos():
          for i in range(len(m_adj_grafo)):
              plt.figure(figsize=(6, 4))
              plt.plot(historico_s[i], label='Suscetíveis', color='blue')
              plt.plot(historico_i[i], label='Infectados', color='red')
              plt.plot(historico_r[i], label='Recuperados', color='green')
              plt.xlabel('Tempo')
              plt.ylabel('População')
              plt.title(f'Evolução da Infecção na Cidade {i}')
              plt.legend()
              plt.show()

          plt.figure(figsize=(6, 4))
          plt.plot(historico_s[-1], label='Suscetíveis', color='blue')
          plt.plot(historico_i[-1], label='Infectados', color='red')
          plt.plot(historico_r[-1], label='Recuperados', color='green')
          plt.xlabel('Tempo')
          plt.ylabel('População')
          plt.title(f'Evolução da Infecção em todas as cidades')
          plt.legend()
          plt.show()

      def desenhar_grafo():
          G = nx.Graph()
          edges = []
          weights = {}
          for i in range(len(m_adj_grafo)):
              for j in range(i + 1, len(m_adj_grafo)):
                  if m_adj_grafo[i][j] > 0:
                      G.add_edge(i, j, weight=m_adj_grafo[i][j])
                      edges.append((i, j))
                      weights[(i, j)] = m_adj_grafo[i][j]

          pos = nx.spring_layout(G)
          node_colors = ['red' if i == indice_mais_influente else 'lightblue' for i in G.nodes()]

          nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', node_size=700)
          nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
          plt.title("Cidade mais influente")
          plt.show()

    # Executar simulação e mostrar gráficos
      desenhar_grafo()
      plotar_graficos()

