class Node:
    """
    Representa um nó na busca do algoritmo A*.

    A prioridade dos nós na fila é baseada no custo total f(n) = g(n) + h(n), e a
    comparação entre nós é definida pela função `__lt__` para uso com filas de prioridade (`heapq`).

    Atributos
    ---------
        value: int 
            valor representando o estado atual.
        g_cost: int
            custo real do início até este nó.
        h_cost: int
            custo estimado até o objetivo (heurística).
        parent: Node
            referência ao nó anterior no caminho.
    """

    def __init__(self, value, g_cost, h_cost, parent=None):
        self.value = value
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent

    def f_cost(self):
        """
        retorna o custo total estimado do nó (f = g + h).

        Retorno
        -------
            f_cost: int
                custo total do nó
        """

        return self.g_cost + self.h_cost

    def __lt__(self, other):
        """
        compara dois nós com base em f(n), para uso na fila de prioridade.

        Parâmetros
        ----------
            other: Node
                nó com o próprio f_cost

        Retorno
        -------
            menor_valor_f_cost: int
                menor valor f_cost comparado a outro nó
        """

        return self.f_cost() < other.f_cost()
