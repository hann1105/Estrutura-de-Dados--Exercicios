"""Implemente uma função para inserir um nó em uma lista encadeada circular de pessoas,
garanƟndo que a ordem crescente por idade seja manƟda. Teste a função para verificar
se a estrutura conƟnua circular após a inserção."""

class Node:
    def __init__(self,idade):
        self.idade=idade
        self.next=None

class Pessoas:
    def __init__(self):
        self.head=None
    
    def inserir(self,idade):
        new_node=Node(idade)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return
        current=self.head
        if idade<self.head.idade:
            while current.next != self.head:
                current=current.next
            current.next=new_node
            new_node.next=self.head
            self.head=new_node
            return
        while current.next !=self.head and current.next.idade<idade:
            current=current.next
        new_node=current.next
        current.next=new_node

    def validar_circularidade(self):
        if self.head is None:
            print("A lista está vazia! E é circular")
            return True
        
        current=self.head.next
        while current is not None and current !=self.head:
            current=current.next
        if current ==self.head:
            print("Lista circular!")
            return True
        else:
            print("Lista não está circular")
            return False

pessoa=Pessoas()
pessoa.inserir(19)
pessoa.inserir(21)
pessoa.inserir(9)
pessoa.inserir(34)
pessoa.inserir(2)
pessoa.validar_circularidade()

        