"""Verificação de Estrutura de Árvore Binária: Implemente uma função que verifique se
uma estrutura de dados representa corretamente uma árvore binária. A função deve
considerar:
a. Se cada nó possui, no máximo, dois filhos.
b. Se não existem ciclos na estrutura.
c. Se a árvore é conectada, ou seja, todos os nós estão acessíveis a parƟr de um
único nó raiz."""


class Node:
    def __init__(self, value):
        self.value = value #valor 
        self.left = None #para o filho da esquerda
        self.right = None #para o filho da direita


def is_binary_tree(root):
    if root is None: #se tiver vazia, ela é binária, por isso o True
        return True

    visited = set() #conjunto para os visitados, para n ter ciclos
    stack = [root] #pilha para percorrer a arvore em profundidade

    while stack:
        node = stack.pop() #remove o último elemento da pilha para visitar

        # Verifica ciclo,Se o ID do nó já tiver sido visitado, significa que a árvore tem um ciclo
        # (um nó aponta de volta para outro já visitado)
        if id(node) in visited:
            return False
        visited.add(id(node)) #marca o nó como visitado

        # Verifica filhos
        filhos = [node.left, node.right] #lista com os filhos do nó
        if len([c for c in filhos if c is not None]) > 2: #se houver mais de dois filhos, ent não é binária
            return False  

        # Continua percorrendo, descendo pela árvore
        if node.left: #se tiver filho à esquerda, adiciona na pilha para verificar dps
            stack.append(node.left)
        if node.right: #se tiver filho à direita, adiciona na pilha para verificar
            stack.append(node.right)

    return True #retorna True, pois é uma árvore binária válida
