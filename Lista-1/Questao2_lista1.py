"""Crie uma função remover_duplicatas(lista), que recebe uma lista encadeada e remove
todas as duplicatas, mantendo apenas a primeira ocorrência de cada elemento. Analise
a complexidade do algoritmo e sugira oƟmizações."""

class Node:
    def __init__(self,dado):
        self.dado=dado
        self.next=None

class Questao2:
    def __init__(self):
        self.head=None
    
    def adicionar(self,dado):
        new_node=Node(dado)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
    
    def remover_duplicatas(self):
        if self.head is None:
            print("Lista vazia")
            return
        
        vistos=set() #conjunto que não aceita duplicadas
        current=self.head #current começa no primeiro nó
        vistos.add(current.dado) #vai adicionar  o produto nos vistos
        
        while current.next is not None: 
            if current.next.dado in vistos: #se o produto do current tiver no conjunto dos vistos
                current.next=current.next.next # vai pular o nó com current.next.next
            
            else:
                vistos.add(current.next.dado) # se não, vai adicionar no conjunto
                current=current.next 
        print("Dados removidos")
    
    def mostrar_lista(self):
        current=self.head
        print("Lista:")
        while current is not None:
            print("-",current.dado)
            current=current.next

lista= Questao2()
lista.adicionar(11)
lista.adicionar(12)
lista.adicionar(11)
lista.adicionar(5)
lista.mostrar_lista()
lista.remover_duplicatas()
lista.mostrar_lista()
