from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        stack = [initial]
        # guarda a menor profundidade em que cada estado foi visto,
        # para poder revisitá-lo se aparecer por um caminho mais curto
        visited = {initial: 0}
        expanded = 0
        generated = 1
        max_frontier = 1

        while stack:
            node = stack.pop()

            if node.is_goal:
                return SearchResult(node, expanded, generated, max_frontier, node.cost)

            if node.cost >= self.depth_limit or node.cost > visited[node]:
                continue

            expanded += 1
            for child in reversed(node.neighbors()):
                generated += 1
                if child.cost < visited.get(child, self.depth_limit + 1):
                    visited[child] = child.cost
                    stack.append(child)

            max_frontier = max(max_frontier, len(stack))

        return SearchResult(None, expanded, generated, max_frontier)