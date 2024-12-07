from typing import List, Tuple


def parse_and_classify(data: str) -> None:
    sections = data.split("\n\n")
    page_rules = [
        tuple(map(int, line.replace("|", ",").split(",")))
        for line in sections[0].split("\n")
    ]
    pages = [list(map(int, line.split(","))) for line in sections[1].split("\n")]

    valid_pages_sum = check_update_order(pages, page_rules)
    print(valid_pages_sum)


def check_update_order(pages: List[List[int]], rules: List[Tuple[int, ...]]) -> int:
    valid_pages = []

    for page in pages:
        is_valid = True
        positions = {page[i]: i for i in range(len(page))}

        for rule in rules:
            if rule[0] in positions and rule[1] in positions:
                if positions[rule[0]] > positions[rule[1]]:
                    is_valid = False
                    break

        if is_valid:
            # Return the middle element in the page list
            mid_value = len(page) // 2
            valid_pages.append(page[mid_value])

    return sum(valid_pages)


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().strip()
        parse_and_classify(data)
