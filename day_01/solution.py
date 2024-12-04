def calculate_distance(a, b) -> int:
    return abs(a - b)


if __name__ == "__main__":

    column_a_index = 0
    column_b_index = 1

    with open("input.txt", "r") as text_file:
        lines = text_file.readlines()
        column_a = []
        column_b = []

        for line in lines:
            parts = line.strip().split()

            column_a.append(int(parts[column_a_index]))
            column_b.append(int(parts[column_b_index]))

        column_a.sort()
        column_b.sort()

        total_distance = 0
        for a, b in zip(column_a, column_b):
            total_distance += calculate_distance(a, b)

        total_similarity_score = 0
        for a in column_a:
            for b in column_b:
                if a == b:
                    total_similarity_score += b

    print(
        f"Total distance: {total_distance}\nTotal similarity score: {total_similarity_score}"
    )
