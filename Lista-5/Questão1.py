"""Pesquisa sobre Aplicações de Árvores: Escolha um tipo de árvore não binária, como
Árvores Rubro-Negras, Árvores B, Árvores de Huffman, Árvores Merkle, ou outras
(exceto AVL). Descreva o conceito, aplicação prática e as principais características que
diferenciam essa estrutura das árvores binárias."""

""" A Árvore de Huffman é uma estrutura usada em algoritmos de compressão de dados sem perdas. Seu 
objetivo é atribuir códigos binários curtos para símbolos mais frequentes e códigos mais longos para 
símbolos menos frequentes, reduzindo o tamanho total da mensagem. A construção da árvore é feita de 
forma ótima, garantindo que não exista outro conjunto de códigos prefixados capaz de gerar uma representação 
mais compacta para a mesma distribuição de frequências. Essa técnica é amplamente utilizada em sistemas de 
compressão, como nos formatos ZIP, GZIP, JPEG, PNG, MP3 e FLAC, além de ser empregada em compiladores para 
otimização de tabelas de símbolos e em protocolos de rede e bancos de dados para reduzir o custo de 
armazenamento e transmissão de dados.

A Árvore de Huffman possui características que a diferenciam das árvores binárias tradicionais. 
Embora seja uma árvore binária, ela não é necessariamente balanceada, pois sua estrutura depende 
diretamente das frequências dos símbolos, e não de regras de balanceamento como as usadas em árvores AVL 
ou Rubro-Negras. Uma de suas principais propriedades é ser uma árvore de prefixo (prefix-free), o que significa
 que nenhum código gerado é prefixo de outro, permitindo uma decodificação simples e sem ambiguidades. 
 A construção da árvore ocorre de forma ascendente (bottom-up), combinando-se repetidamente os dois símbolos 
 menos frequentes até restar apenas um nó raiz, e cada nó contém um peso que representa a soma das frequências 
 de seus filhos. Com isso, a Árvore de Huffman garante uma compressão ótima dentro da categoria de códigos 
 prefixados.

Essa estrutura se diferencia das árvores binárias comuns também quanto ao propósito. Enquanto árvores binárias 
tradicionais são usadas principalmente para busca e organização de dados, a Árvore de Huffman tem como foco 
exclusivo a compressão eficiente. Além disso, árvores binárias comuns armazenam apenas valores ou chaves, 
enquanto a Árvore de Huffman armazena pesos e símbolos associados às suas frequências. Por essas razões, a 
Árvore de Huffman é uma ferramenta essencial em diversos sistemas modernos de compressão e continua sendo uma
das técnicas mais eficientes e utilizadas quando o objetivo é reduzir o tamanho dos dados sem perder informação."""