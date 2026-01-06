"""Implemente um código para criação de filas com prioridade, que remove os elementos
com base nesta prioridade. Em relação às filas tradicionais, faz mais sentido (do ponto
de vista computacional) ajustar a fila na inserção ou na remoção?"""
class Node:
    def __init__(self,valor,prioridade):
        self.valor=valor
        self.prioridade=prioridade
        self.next=None

class Fila_Prioridade:
    def __init__(self):
        self.front=None
        self._size=0
    def is_empty(self):
        return self.front is None
    def enqueue(self,valor,prioridade):
        new_node=Node(valor,prioridade)
        if self.is_empty() or prioridade>self.front.prioridade:
            new_node.next=self.front
            self.front=new_node
        else:
            current=self.front
            while current.next and current.next.prioridade>=prioridade:
                current=current.next
            new_node.next=current.next
            current.next=new_node
        self._size+=1
        print(f"Inserido:{valor}-Prioridade:{prioridade}")
    def dequeue(self):
        if self.is_empty():
            return None
        valor=self.front.valor
        self.front=self.front.next
        self._size-=1
        return valor
    def mostrar(self):
        current=self.front
        fila=[]
        while current:
            fila.append(f"{current.valor}({current.prioridade})")
            current=current.next
        return "->".join(fila)

fila=Fila_Prioridade()
fila.enqueue("Idoso",10)
fila.enqueue("Jovem",4)
fila.enqueue("Adulto",6)
print(f"Fila atual: {fila.mostrar()}")
print(f"Removido:{fila.dequeue()}")

#Melhor ajustar na inserção pois assim quando tiver a remoção já estará em ordem e com o 
#valor certo a se remover, sem precisar percorrer a lista toda para ver quem tem prioridade