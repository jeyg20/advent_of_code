import re


def get_uncorrupted_data(data: str):
    # Matches all valid mul instructions and extracts their operands
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    return sum(int(x) * int(y) for x, y in mul_pattern.findall(data))


def part_two(input_string: str):
    # Match control and mul instructions together
    instruction_pattern = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")
    suppress = False
    result = 0

    # Iterate over all matches in order
    for match in instruction_pattern.finditer(input_string):
        if match.group(0) == "do()":
            suppress = False  # Enable future mul instructions
        elif match.group(0) == "don't()":
            suppress = True  # Disable future mul instructions
        else:  # Handle mul(X,Y)
            if not suppress:
                x, y = map(int, match.groups())
                result += x * y

    return result


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
        result_1 = get_uncorrupted_data(data)
        result_2 = part_two(data)

        print("Result Part One:", result_1)
        print("Result Part Two:", result_2)
