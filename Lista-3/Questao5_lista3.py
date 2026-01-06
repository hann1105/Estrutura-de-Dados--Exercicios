"""(Discursiva) Imagine que você é o gerente de uma empresa de entrega de
encomendas e precisa oƟmizar o tempo de entrega para saƟsfazer seus clientes.
Você decidiu desenvolver um algoritmo para determinar a melhor rota de entrega
para cada motorista, levando em consideração os locais de coleta e entrega das
encomendas. Sabendo que a complexidade algorítmica afeta diretamente o
desempenho do algoritmo, descreva uma proposta para seus programadores,
considerando a análise da complexidade uƟlizando a notação Big O. Não precisa de
código, porém é preciso discuƟr:
a. A importância de considerar a complexidade algorítmica na escolha do
algoritmo para oƟmizar as rotas de entrega.
b. Como a notação Big O pode ser usada para comparar diferentes algoritmos e
determinar qual deles é mais eficiente em termos de tempo de execução."""

#a)
""" Analisar qual algoritmo é melhor para determinar problemas é crucial para um bom desempenho do código
pois, cada algoritmo tem um desempenho particular e que mais se adequa a cada aplicação, dito isso, considerar
a complexidade algorítmica é crucial na escolha para otimizar as rotas de entrega, pois se escolher um algoritmo
com complexidade elevada, como O(2^n), o tempo de execução vai acabar se tornando inviável, a medida que o número
das encomendas cresce, e assim iria atrasar as entregas. Então Por outro lado, algoritmos com complexidade menor, como 
O(n logn) ou O(n²), tendem a escalar melhor e permitem processar um grande volume de dados em tempo razoável, 
garantindo que as rotas sejam calculadas de forma eficiente mesmo com muitos pontos de coleta e entrega. Por isso
é necessário ter essa análise de qual método utilizar. """

#b)
"""notação Big O é uma ferramenta essencial nesse processo, pois ela descreve o comportamento do 
tempo de execução do algoritmo em função do tamanho da entrada. Ao comparar diferentes algoritmos,
é possível prever qual deles será mais eficiente em cenários com grande quantidade de dados, sem precisar
implementá-los completamente.Então, ter a Notação Big O, para ajudar na análise de qual algoritmo escolher
é muito importante, visto que não é só resolver a solução, mas também ver a eficiência do código, inclsuive no pior caso"""

#Então, a proposta é criar um algoritmo que consiga ser trabalhado com grandes volumes de dados e também que seja rápido para 
#processá-los, facilitando e otimizando as entregas além de agradar os clientes pela rapidez. Esse algoritmo deverá ser
# estudado e analizado de acordo com a sua complexidade utilizando a notação Big 0, já que é uma ferramenta principal para analisar
#os melhores algoritmos