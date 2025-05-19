from a_star import AStar

class Main:
    """
    Classe principal responsável por executar o algoritmo A*.

    Solicita ao usuário os valores de início e objetivo, executa o algoritmo
    e exibe o caminho encontrado, o número de nós visitados e o custo total.
    """
    
    @staticmethod
    def run():
        start = int(input("Digite o número inicial: "))
        goal = int(input("Digite o número objetivo: "))
        astar = AStar(start, goal)
        result = astar.find_path()

        if result:
            print("Caminho percorrido:", result["path"])
            print("Quantidade de nós visitados:", result["nodes_visited"])
            print("Custo total:", result["total_cost"])
        else:
            print("Não foi possível encontrar um caminho.")


if __name__ == "__main__":
    Main.run()
