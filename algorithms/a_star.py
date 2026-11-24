import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        # distância de Manhattan de cada peça até a posição dela no objetivo
        distance = 0
        for i, tile in enumerate(state.tiles):
            if tile != 0:
                goal = GOAL_STATE.index(tile)
                distance += abs(i // 3 - goal // 3) + abs(i % 3 - goal % 3)
        return distance

    def search(self, initial: State) -> SearchResult:
        frontier = [(self.heuristic(initial), initial)]
        explored = set()
        expanded = 0
        generated = 1
        max_frontier = 1

        while frontier:
            _, node = heapq.heappop(frontier)

            if node in explored:
                continue

            if node.is_goal:
                return SearchResult(node, expanded, generated, max_frontier, node.cost)

            explored.add(node)
            expanded += 1
            for child in node.neighbors():
                generated += 1
                if child not in explored:
                    f = child.cost + self.heuristic(child)
                    heapq.heappush(frontier, (f, child))

            max_frontier = max(max_frontier, len(frontier))

        return SearchResult(None, expanded, generated, max_frontier)