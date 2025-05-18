import heapq

"""
classe para representar os nós
Node {
    valor do nó,
    custo real até o nó,
    cálculo da heurística,
    nó pai
}
"""
class Node:
    def __init__(self, value, g_cost, h_cost, parent):
        self.value = value
        self.g_cost = g_cost 
        self.h_cost = h_cost 
        self.parent = parent 

    def f_cost(self):
        return self.g_cost + self.h_cost

    """define a prioridade na fila (menor custo f(n))"""
    def __lt__(self, other):
        return self.f_cost() < other.f_cost()

"""
heurística simples (diferença absoluta entre os valores)
"""
def heuristic(current, goal):
    return abs(goal - current)

"""
algoritmo de busca

descrição: Encontrar o menor caminho entre start_value e goal_value usando apenas as operações permitidas: +1 e *2.
"""
def a_star(start_value, goal_value):
    open_set = []
    heapq.heappush(open_set, Node(start_value, 0, heuristic(start_value, goal_value), None))
    visited = set()
    nodes_visited = 0

    while open_set:
        current = heapq.heappop(open_set)
        nodes_visited += 1

        """condição de parada (reconstruir o caminho)"""
        if current.value == goal_value:
            path = []
            node = current
            while node:
                path.append(node.value)
                node = node.parent
            path.reverse()

            print("Caminho percorrido:", path)
            print("Quantidade de nós visitados:", nodes_visited)
            print("Custo total:", current.g_cost)
            return

        visited.add(current.value)

        """gera os próximos estados (+1 e *2)"""
        for next_value in [current.value + 1, current.value * 2]:
            if next_value not in visited and next_value <= goal_value * 2:  
                next_node = Node(
                    next_value,
                    current.g_cost + 1,
                    heuristic(next_value, goal_value),
                    current
                )
                heapq.heappush(open_set, next_node)

    print("Não foi possível encontrar um caminho.")

"""
função main
"""
if __name__ == "__main__":
    start = int(input("Digite o número inicial: "))
    goal = int(input("Digite o número objetivo: "))
    a_star(start, goal)
