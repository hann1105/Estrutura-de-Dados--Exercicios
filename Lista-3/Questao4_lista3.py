"""Escreva um código em Python para verificar se uma lista contém algum par de
elementos cuja soma seja igual a um valor específico. Qual é a complexidade de
tempo desse algoritmo? Explique o porquê. Faça uma análise da complexidade."""

def verificar(lista,valor):
    tamanho=len(lista)
    par=False #Ela será usada para saber se pelo menos um par de números que some o valor pedido.
    for i in range(tamanho): # loop externo para percorrer cada elemento da lista, i é o primeiro elemento do par
        for j in range(i+1,tamanho): #percorre todos os elementos à frente do elemento i e j é o 2° elemento do par
            if lista[i]+lista[j]==valor:
                print(f"O par ({lista[i]},{lista[j]}) formam a soma do valor pedido")
                par=True
    if not par:
        print("Não há um par de elementos na lista em que a soma dê o valor pedido")
        
    
#testando:
if __name__ == "__main__":
    lista=[1,2,3,4,5,10,23,18,11,13,37,24,0]
    usuario=int(input("Digite o valor da soma desejada: "))
    verificar(lista,usuario)

"""A complexidade de tempo do algoritmo é O(n²), onde n é o número de elementos da lista.
Isso ocorre porque o algoritmo percorre todos os pares possíveis da lista usando dois loops aninhados.
O primeiro loop percorre todos os elementos da lista, e o segundo loop percorre todos os elementos restantes para formar pares.
Portanto, para uma lista de tamanho n, o número de comparações é aproximadamente n(n-1)/2, o que cresce de forma quadrática conforme o tamanho da lista aumenta.
Em termos práticos, isso significa que se o tamanho da lista dobrar, o número de operações aumenta aproximadamente quatro vezes."""
        #no total, o número de iterações é:(n-1) + (n-2) + (n-3) + ... + 1 e é quadrático pq cada elemento da lista é comparado com todos os outros elementos que vêm depois dele.