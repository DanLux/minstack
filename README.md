
# Min Stack

> Implementação de uma pilha de inteiros onde cada uma das operações disponibilizada é executada em O(1)


### Operações disponíveis

- push: places new value on top of the stack
- pop: takes the value on top of the stack
- min: returns the minimum value in the whole stack


### Funcionamento

A estrutura funciona através do uso de duas pilhas de inteiros. A primeira guarda todos os inteiros adicionados e removidos através dos métodos push e pop.

Já a segunda pilha é responsável por armazenar o valores mínimos e é consultada pelo método min. Sendo assim, o i-ésimo valor presente na segunda pilha sempre equivale ao menor valor presente entre os primeiros i elementos da primeira pilha.

As operações são constantes pois não há laços condicionais nos métodos. E, independente do tamanho da pilha atual, os três métodos efetuam o mesmo número constante de operações.