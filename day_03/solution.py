import re


def get_uncorrupted_data(data: str):
    patter = r"mul\(\d+,\d+\)"

    uncorrupted_data = re.findall(patter, data)

    operands = [
        item.replace("mul(", "").replace(",", " ").replace(")", "").split()
        for item in uncorrupted_data
    ]

    result: int = 0
    for number in operands:
        result += int(number[0]) * int(number[1])
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
        result = 0
        for line in lines:
            result += get_uncorrupted_data(line)

        print(result)
