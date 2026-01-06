"""Crie duas Pilhas com diferentes implementações: Uma usando collections.deque, e
a outra usando Lista Encadeadas. Faça inserções e remoções nas pilhas criadas na
questão anterior e discuta qual das duas implementações aparenta ser mais
eficiente e o porquê."""
from collections import deque
class PilhaDeque:
    def __init__(self):
        self.itens=deque()
    
    def push(self,elemento):
        self.itens.append(elemento)
        
    
    def pop(self):
        return self.itens.pop()
    
    def exibir_pilha(self):
        return (f"Pilha: {self.itens}")
    
# Pilha com Lista encadeada

class Node:
    def __init__(self,dado):
        self.dado=dado
        self.next=None

class PilhaEncadeada:
    def __init__(self):
        self.topo=None
    def push(self,elemento):
        new_node=Node(elemento)
        new_node.next=self.topo
        self.topo=new_node
    def pop(self):
        if self.is_empty():
            print("Pilha vazia")
            return
        valor=self.topo.dado #guarda o valor
        self.topo=self.topo.next 
        return valor
    def is_empty(self):
        return self.topo is None
    
    def exibir(self):
        if self.topo is None:
            print("Pilha vazia")
            return
        current = self.topo
        print("Topo - ",end="")
        while current is not None:
            print(current.dado, end=" - ")
            current = current.next
        print("fim")
        return


#Teste
    
pilha=PilhaDeque()
pilha.push(11)
pilha.push(5)
print(pilha.exibir_pilha())
pilha.pop()
print(pilha.exibir_pilha())

print("Pilha com lista encadeada")
p = PilhaEncadeada()
p.push(11)
p.push(12)
p.exibir()

#A pilha com lista encadeada ocupa mais memória do que a com deque, pois a cada nó ele cria um novo objeto
# isso faz com que a pilha usando deque seja mais eficiente e com pouco consumo de memória já que já é uma biblioteca da própria linguagem
