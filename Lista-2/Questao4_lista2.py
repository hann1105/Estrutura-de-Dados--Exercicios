"""Escreva uma função em Python que recebe uma pilha como entrada e inverte a
ordem dos elementos utilizando apenas uma pilha adicional."""
class Pilha:
    def __init__(self):
        self.itens=[] #lista para guardar os elementos da pilha
    
    def push(self,elemento):
        self.itens.append(elemento)
    
    def pop(self):
        if not self.vazia():
            return self.itens.pop() #vai remover o primeiro elemento da pilha e mostrar
        return None
    
    def vazia(self):
        return len(self.itens)==0
    
    def mostrar(self):
        if not self.vazia():
            for elemento in self.itens:
                print(elemento)
            return
        else:
            print("Pilha vazia")
            return
    
    
def inverter(pilha):
    auxiliar=Pilha()
    while not pilha.vazia():
        auxiliar.push(pilha.pop()) #vai pegar os primeiros elementos da pila inicial e vai colocar como últimos na pilha auxiliar
    return auxiliar

pilha1=Pilha()
pilha1.push(5)
pilha1.push(11)
pilha1.push(12)
pilha1.push(50)
pilha1.mostrar()

invertida=inverter(pilha1)
print("Invertida:")
invertida.mostrar()






    