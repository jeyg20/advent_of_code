def calculate_total_safe_reports(levels: list[int]) -> bool:
    for i in range(len(levels) - 1):
        if not (1 <= abs(levels[i + 1] - levels[i]) <= 3):
            return False

    increasing, decreasing = True, True
    for i in range(1, len(levels)):
        if levels[i] > levels[i - 1]:
            decreasing = False
        elif levels[i] < levels[i - 1]:
            increasing = False

    return increasing or decreasing


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        part_one_safe_reports = 0
        part_two_safe_reports = 0
        for line in input_file:
            levels = [int(num) for num in line.split()]
            if calculate_total_safe_reports(levels):
                part_one_safe_reports += 1
            else:
                for i in range(0, len(levels)):
                    levels_copy = levels[:]
                    levels_copy.pop(i)
                    if calculate_total_safe_reports(levels_copy):
                        part_two_safe_reports += 1
                        break

        print(part_one_safe_reports)
        print(part_one_safe_reports + part_two_safe_reports)
