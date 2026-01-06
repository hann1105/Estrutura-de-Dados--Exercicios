
"""Implemente uma fila circular utilizando um deque. A fila circular possui um tamanho
máximo e, quando atinge esse tamanho, o próximo elemento a ser inserido subsƟtui
o elemento mais antigo da fila. Crie funções para inserir elementos na fila (enqueue),
remover elementos da fila (dequeue) e exibir os elementos da fila."""
class Node:
    def __init__(self,dado):
        self.dado=dado
        self.next=None
        self.prev=None

class FilaCircularDequeEncadeado:
    def __init__(self,capacidade):
        self.capacidade=capacidade
        self.front=None
        self.tail=None
        self.tamanho=0
    
    def esta_cheia(self):
        return self.tamanho==self.capacidade
    
    def enqueue(self,dado):
        new_node=Node(dado)

        if self.esta_cheia():
            self.dequeue() #vai tirar o elemento mais antigo
            
        if self.front is None:
            self.front=self.tail=new_node
            self.front.next=self.front # o próximo da cabeça é a cabeça para ser circular
            self.front.prev=self.front 

        else:
            new_node.prev=self.tail #o anterior do novo é o último
            new_node.next=self.front #circular, o proximo do novo é a cabeça
            self.tail.next=new_node #o proximo ultimo será o novo nó
            self.front.prev=new_node # e o anterior do front é o novo nó, logo o último é o novo nó
            self.tail=new_node

        self.tamanho+=1
    
    def dequeue(self):
        valor=self.front.dado #para mostrar o valor no return
        if self.front==self.tail: #tem só um elemento, vai excluir ele e voltar a ser None, lista fica vazia
            self.front=self.tail=None
        else:
            self.front=self.front.next #o front será o seu proximo já que tira do inicio
            self.front.prev=self.tail #o prev do front vai ser o último 
            self.tail.next=self.front #o proximo do ultimo será o novo front
        self.tamanho-=1
        return valor
    
    def exibir_elementos(self):
        if self.front==None:
            print("Fila vazia")
            return
        current=self.front
        elementos=[]
        for _ in range(self.tamanho):
            elementos.append(current.dado)
            current = current.next
        print(f"Fila: {elementos}")


#Testando
"""fila = FilaCircularDequeEncadeado(4)

fila.enqueue(1)
fila.enqueue(5)
fila.enqueue(11)
fila.exibir_elementos()   

fila.enqueue(12)   
fila.exibir_elementos() 
fila.enqueue(25) 
fila.exibir_elementos()

print(f"Removido:{fila.dequeue()}")  
fila.exibir_elementos()   
"""
    
            

