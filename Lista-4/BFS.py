from collections import deque
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, matriz):
        """
        Inicializa um grafo usando uma matriz de adjacência pronta.
        """
        self.matriz = matriz
        self.n = len(matriz)  # número de vértices

    def bfs(self, origem):
       
        visitado = set() #conjunto para colocar os nós ja visitados
        fila = deque([origem]) #fila para colocar os vizinhos e ja coloca o nó origem dentro como o primeiro

        distancia = {v: float("inf") for v in range(self.n)} #a distancia começa com infinito ja que os nós n foram descobertos ainda
        distancia[origem] = 0 #distancia do primeiro nó é 0

        pai = {v: None for v in range(self.n)} #o pai é o nó anterior ao atual
        ordem = [] #lista para colocar a ordem de visitas

        while fila: #loop principal do BFS, enquanto tiver elementos na fila
            atual = fila.popleft() #vai tirar o nó atual da fila
            ordem.append(atual) #vai adicionar tanto na lista de ordem de visita quanto no conjunto de visitas
            visitado.add(atual)

            # percorre vizinhos olhando a matriz
            for vizinho in range(self.n): #percorre os vizinhos ao lado 
                if self.matriz[atual][vizinho] == 1 and vizinho not in visitado: #se existe aresta entre atual e vizinho
                    visitado.add(vizinho) # e o vizinho ainda não foi visitado, adiciona no conjunto,
                    distancia[vizinho] = distancia[atual] + 1 #a distancia do vizinho é a distancia do atual +1
                    pai[vizinho] = atual #o nó atual é o pai/predecessor do vizinho
                    fila.append(vizinho) #adiciona o vizinho na fila para continuar o BFS

        return distancia, pai, ordem

    def reconstruir_caminho(self, pai, origem, destino): #Reconstrói o caminho mínimo entre origem e destino.
        if pai[destino] is None and origem != destino: #Se o destino não tem pai,e n é a origem, não existe caminho.
            return []  # destino inalcançável

        caminho = [] #lista vazia caminho que armazenará os vertices do caminho.
        atual = destino

        while atual is not None:
            caminho.append(atual) #Vai seguindo os pais até chegar na origem
            atual = pai[atual]

        return caminho[::-1]  # inverte para começar da origem

    def desenhar(self, pos, distancia, caminho,rotulos): #Desenha o grafo e marca o caminho mínimo usando cores.
        
        plt.figure(figsize=(10, 7)) #Tamanho da imagem

        # desenha arestas
        for u in range(self.n): #pega a posição do nó u
            x1, y1 = pos[u]
            for v in range(self.n): #ve todos os vizinhos possiveis
                if self.matriz[u][v] == 1 and u<v: #existe uma aresta entre u e v
                    x2, y2 = pos[v]
                    # Se a aresta fizer parte do caminho mínimo → azul, senão cinza
                    if (u in caminho and v in caminho and abs(caminho.index(u) - caminho.index(v)) == 1):
                        cor = "blue"
                        largura = 3
                    else:
                        cor = "gray"
                        largura = 1.5

                    plt.plot([x1, x2], [y1, y2], color=cor, linewidth=largura)

        # Cor única para todos os nós
        cor_no = "#1f78b4"  # azul bonito uniforme

        #desenha nós
        for v, (x,y) in pos.items():
            plt.scatter(x, y, s=900, color=cor_no, edgecolors="black", linewidth=2)
            plt.text(x, y, rotulos[v], fontsize=18, ha="center", va="center", fontweight="bold")
            plt.text(x, y-0.25, f"d={distancia[v]}", fontsize=11, ha="center")

        plt.title("BFS", fontsize=16)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

def traduzir_lista(lista, rotulos):
    return [rotulos[v] for v in lista]

def traduzir_dicionario(dicionario, rotulos):
    return {rotulos[k]: rotulos[v] if v is not None else None for k, v in dicionario.items()}


if __name__ == "__main__":
    
    matriz = [
        # A B C D E F G H
        [0,1,1,0,0,0,0,0], # A
        [1,0,1,1,0,0,0,0], # B
        [1,1,0,0,1,0,0,0], # C
        [0,1,0,0,1,1,0,0], # D
        [0,0,1,1,0,1,1,0], # E
        [0,0,0,1,1,0,0,1], # F
        [0,0,0,0,1,0,0,1], # G
        [0,0,0,0,0,1,1,0], # H
    ]

    g = Grafo(matriz) #cria o grafo com a matriz 

    origem = 0
    distancia, pai, ordem = g.bfs(origem)

    destino = 7
    caminho = g.reconstruir_caminho(pai, origem, destino)
    print(f"Caminho mínimo até {destino}:", caminho)

    # posições dos nós para desenhar
    pos = {
        0:(0,3), 1:(-2,2), 2:(2,2), 3:(-2,1), 4:(2,1), 5:(-1,0), 6:(3,0), 7:(0,-1)
    }

    # rótulos para mostrar no gráfico (0->A, 1->B, ...)
    rotulos = {0: 'A',1: 'B',2: 'C',3: 'D',4: 'E',5: 'F',6: 'G', 7:'H'}

    print("Ordem de visita:", traduzir_lista(ordem, rotulos))
    print("Pais:", traduzir_dicionario(pai, rotulos))
    print("Distâncias :")
    for v in distancia:
        print(f"  {rotulos[v]}: {distancia[v]}")

    g.desenhar(pos, distancia, caminho,rotulos)
