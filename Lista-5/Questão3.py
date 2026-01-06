"""Inserção e Exclusão em Árvores Binárias: Implemente funções para realizar operações
de inserção e exclusão em uma árvore binária de busca. Garanta que os elementos sejam
organizados de acordo com as regras de uma árvore binária de busca (onde o nó
esquerdo contém valores menores e o nó direito valores maiores)."""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None #parte esquerda
        self.right = None #parte direita


class BinarySearchTree:
    def __init__(self):
        self.root = None #raiz, arvore vazia

    def insert(self, value):
        new_node = Node(value) #novo nó com valor

        if self.root is None: 
            self.root = new_node #se a árvore tiver vazia, o novo nó sera a raiz
            return

        current = self.root #current para percorrer a árvore toda até achar o lugar do novo nó

        while True:
            if value < current.value:  # se o valor for menor que o current, vai para a esquerda
                if current.left is None:  #se for None, o novo nó ficará no lugar e encerra
                    current.left = new_node
                    return
                current = current.left #se não, atualiza e continua a busca

            else:  # vai para direita (>=)
                if current.right is None: #se right for None, colocar o novo nó e encerra
                    current.right = new_node
                    return
                current = current.right #caso não, atualiza o current e continua


    # Função auxiliar para encontrar o menor valor da subárvore direita
    def min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Remoção (3 casos principais)
    def remove(self, value): #remove chamando o método recursivo
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, node, value):

        if node is None: #se tiver vazia, retorna None
            return None

        # Busca o nó
        if value < node.value: #se for menor, que o node.valor, vai para a parte esquerda
            node.left = self._remove_recursive(node.left, value)

        elif value > node.value: #se for maior, para a parte direita, recursivamente
            node.right = self._remove_recursive(node.right, value)

        else: #achou o nó que será removido
            # Caso 1: nó folha
            if node.left is None and node.right is None:
                return None #vai ser removido e vira None

            # Caso 2: um filho
            if node.left is None: #o pai é removido e o filho que será o nó
                return node.right #substitui pelo filho direito
            if node.right is None:
                return node.left #substitui pelo filho esquerdo

            # Caso 3: dois filhos
            minimo = self.min_node(node.right) #encontra o menor valor da árvore
            node.value = minimo.value
            node.right = self._remove_recursive(node.right, minimo.value)

        return node

    # Percurso in-order (ordem crescente)
    def inorder(self): #para mostrar com o print
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result) #mostra o esquerdo
            result.append(node.value) #a raiz
            self._inorder_recursive(node.right, result) #mostra o direito

#testando
bst = BinarySearchTree()

bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)

print("In-order:", bst.inorder())  # [1,3,6,8,10]

bst.remove(3)
print("Após remover 3:", bst.inorder())
