def parse_and_classify(data: str):
    sections = data.split("\n\n")
    page_rules = [
        tuple(map(int, line.replace("|", ",").split(",")))
        for line in sections[0].split("\n")
    ]
    pages = [list(map(int, line.split(","))) for line in sections[1].split("\n")]

    check_updates(pages, page_rules)


def check_updates(pages: list, rules: list):
    valid_pages: list = []

    for page in pages:
        is_valid = True
        for rule in rules:
            if rule[0] in page and rule[1] in page:
                if page.index(rule[0]) > page.index(rule[1]):
                    is_valid = False
                    break

        if is_valid:
            mid_value = len(page) // 2
            valid_pages.append(page[mid_value])
    print(sum(valid_pages))


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().strip()
        parse_and_classify(data)
