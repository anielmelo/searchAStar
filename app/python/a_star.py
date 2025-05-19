import heapq
from node import Node

class AStar:
    """
    Implementação do algoritmo A* (A-Star) para encontrar o menor caminho entre dois números
    inteiros utilizando operações específicas (+1 e *2).

    O objetivo é transformar um número inicial (start_value) em um número alvo (goal_value).

    A busca utiliza uma fila de prioridade (heapq) para explorar os nós com o menor custo estimado
    até o objetivo.

    Atributos
    ---------
        start_value: int
            valor inicial da busca.
        goal_value: int
            valor objetivo da busca.
        open_set: list
            fila de prioridade contendo os nós a serem explorados.
        visited: set()
            conjunto de valores já visitados.
        nodes_visited: int
            contador de nós visitados durante a execução.
    """

    def __init__(self, start_value, goal_value):
        self.start_value = start_value
        self.goal_value = goal_value
        self.open_set = []
        self.visited = set()
        self.nodes_visited = 0

    def heuristic(self, current):
        """
        calcula a heurística baseada na diferença absoluta entre o valor atual e final.

        Parâmetros
        ----------
            current: int
                valor do nó atual.

        Retorno
        -------
            h_cost: int
                valor da diferença entre valor atual e final.
        """

        return abs(self.goal_value - current)

    def find_path(self):
        """
        executa o algoritmo A* e retorna o caminho até o objetivo (se houver).

        Retorno
        -------
            reconstruct_path: dict
                chama o dict retornado pelo metódo de reconstrução de caminho até o valor final.
        """

        start_node = Node(
            self.start_value,
            g_cost=0,
            h_cost=self.heuristic(self.start_value)
        )
        heapq.heappush(self.open_set, start_node)

        while self.open_set:
            current = heapq.heappop(self.open_set)
            self.nodes_visited += 1

            if current.value == self.goal_value:
                return self.reconstruct_path(current)

            self.visited.add(current.value)

            for next_value in [current.value + 1, current.value * 2]:
                if next_value not in self.visited and next_value <= self.goal_value * 2:
                    next_node = Node(
                        next_value,
                        g_cost=current.g_cost + 1,
                        h_cost=self.heuristic(next_value),
                        parent=current
                    )
                    heapq.heappush(self.open_set, next_node)

        return None

    def reconstruct_path(self, node):
        """
        reconstrói o caminho do nó inicial até o nó final.

        Parâmetros
        ----------
            node: Node
                nó atual

        Retorno
        -------
            dicionário contendo o caminho do nó inicial até o nó final, o número de nós visitados e o custo total para chegar até o nó final.
        """
        
        path = []
        while node:
            path.append(node.value)
            node = node.parent
        path.reverse()
        return {
            "path": path,
            "nodes_visited": self.nodes_visited,
            "total_cost": len(path) - 1
        }
