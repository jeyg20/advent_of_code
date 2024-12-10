from collections import deque
from typing import Dict, List, Tuple


def parse_and_classify(data: str) -> Tuple[int, int]:
    sections = data.strip().split("\n\n")
    page_rules = [tuple(map(int, line.split("|"))) for line in sections[0].split("\n")]
    updates = [list(map(int, line.split(","))) for line in sections[1].split("\n")]

    def process_update(update: List[int]) -> Tuple[bool, int]:
        relevant_rules = [(x, y) for x, y in page_rules if x in update and y in update]
        graph = create_graph(relevant_rules, update)
        sorted_order = topological_sort(graph, set(update))

        positions = {page: i for i, page in enumerate(sorted_order)}
        update_positions = [positions[page] for page in update]

        is_valid = all(
            update_positions[i] <= update_positions[i + 1]
            for i in range(len(update_positions) - 1)
        )
        reordered_update = (
            update if is_valid else sorted(update, key=lambda page: positions[page])
        )
        mid_page = reordered_update[len(reordered_update) // 2]

        return is_valid, mid_page

    part1_mid_values, part2_mid_values = [], []

    for update in updates:
        is_valid, mid_page = process_update(update)
        if is_valid:
            part1_mid_values.append(mid_page)
        else:
            part2_mid_values.append(mid_page)

    return sum(part1_mid_values), sum(part2_mid_values)


def create_graph(
    rules: List[Tuple[int, int]], pages_in_update: List[int]
) -> Dict[int, List[int]]:
    graph = {page: [] for page in pages_in_update}
    for x, y in rules:
        graph[x].append(y)
    return graph


def topological_sort(graph: Dict[int, List[int]], all_pages: set) -> List[int]:
    """
    Perform Kahn's Algorithm for topological sorting.
    """
    in_degree = {node: 0 for node in all_pages}
    for neighbors in graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    queue = deque(node for node in all_pages if in_degree[node] == 0)
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)

        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read()
        part1_result, part2_result = parse_and_classify(data)
        print("Part 1:", part1_result)
        print("Part 2:", part2_result)
