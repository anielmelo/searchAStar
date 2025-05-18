# searchAStar

Solução que implementa o **algoritmo de busca A*** para encontrar o caminho mais eficiente de um número inicial até um número objetivo utilizando apenas as operações permitidas:
- Adição de 1 (+1)
- Multiplicação por 2 (*2)

### O algoritmo tenta encontrar o menor número de passos para transformar o número inicial no número objetivo.

- **Custo real (g(n)):** número de operações realizadas até o momento.
- **Heurística (h(n)):** diferença entre o valor atual e o valor objetivo.
- **Custo total (f(n) = g(n) + h(n)):** estimativa do custo do caminho completo, usada para priorizar a busca.

### Exemplo de saída:

```sh
Digite o número inicial: 1
Digite o número objetivo: 9
Caminho percorrido: [1, 2, 4, 8, 9]
Quantidade de nós visitados: 5
Custo total: 4
```