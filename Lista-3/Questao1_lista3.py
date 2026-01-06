""" O algoritmo Quick Sort é conhecido por ter uma boa eficiência na práƟca, mas seu
pior caso pode ser lento. Como é possível melhorar o desempenho do Quick Sort em
casos específicos? Discuta a estratégia do "QuickSort mediana de três"."""



"""o Quick Sort no seu pior caso fica com complexidade O (N²), isso acontece devido a má escolha do pivô, como por
exemplo se pegar o pivo muito alto ou muito menor, o que deixaria as separações do quicksort desequilibradas, logo
para melhorar isso e escolher um bom pivô existe a estratégia da mediana de tres, em que se pega o valor do início,
o valor do meio da lista e o valor final, e faz-se a mediana entre eles, assim escolhe o elemento que está no meio desses 
três elementos 'ordenados', isso ajuda a escolher um pivô que esteja mais perto do valor do verdadeiro meio da lista ordenada
assim deixa as separações mais equilibradas e não precisa fazer tantas comparações ja que é uma estratégia de deixar a lista
mais organizada antes de realmente estar em ordem"""

def mediana_tres(arr,inicio,fim):
    meio=(inicio+fim)//2 #dividindo os elementos em inicio, meio e fim
    a=arr[inicio]
    b=arr[meio]
    c=arr[fim]
    
    #ordenar e trocar a ordem desses valores para deixá-los ordenados entre si
    if a>b: #se o inicio for maior que o meio
        arr[inicio],arr[meio]=arr[meio],arr[inicio]
    if a>c: #se o inicio for maior que o fim
        arr[inicio],arr[fim]=arr[fim],arr[inicio]
    if b>c: #se o meio for maior que o fim
        arr[meio],arr[fim]=arr[fim],arr[meio]

    #o pivo é o meio
    return b

def quicksort(arr):
    if len(arr) <= 1: #se o tamanho for =1 ou menor ja está ordenado
        return arr
    
    # chama a função de mediana de três
    pivô = mediana_tres(arr,0, len(arr) - 1) #o pivo é a mediana de tres, 0 como inicio e len(arr)-1 como fim

    # cria as sublistas
    left = [x for x in arr if x < pivô] #esquerda, menores que o pivô
    middle = [x for x in arr if x == pivô] #meio
    right = [x for x in arr if x > pivô]#direita,maiores que o pivô

    # recursão
    return quicksort(left) + middle + quicksort(right)

#testando
arr=[5,11,5,9,12,4,2]
print(f"lista sem ser ordenada: {arr}")
arr=quicksort(arr)
print(f"lista ordenada: {arr}")