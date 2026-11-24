"""Script de demonstração — útil para depurar manualmente."""

from puzzle.state import State
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.a_star import AStar


def print_result(name: str, result):
    print(f"\n{'='*40}")
    print(f"Algoritmo : {name}")
    if result.found:
        print(f"Solução   : {' → '.join(result.actions)}")
        print(f"Custo     : {result.path_cost}")
        print(f"Profund.  : {result.depth}")
    else:
        print("Solução   : NÃO ENCONTRADA")
    print(f"Expandidos: {result.nodes_expanded}")
    print(f"Gerados   : {result.nodes_generated}")
    print(f"Fronteira : {result.max_frontier_size} (máx)")


def run_all(initial: State):
    print("\nEstado inicial:")
    print(initial)

    print_result("BFS",  BFS().search(initial))
    print_result("DFS",  DFS().search(initial))
    print_result("A*",   AStar().search(initial))


if __name__ == "__main__":
    # 20 movimentos até a solução
    run_all(State((7, 2, 4, 5, 0, 6, 8, 3, 1)))

    # sem solução: não é possível chegar ao objetivo a partir deste estado
    run_all(State((2, 8, 3, 1, 6, 4, 7, 0, 5)))