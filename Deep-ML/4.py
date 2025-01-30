# Calculate Mean by Row or Column
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

    if mode == "column":
        # zip() to get all elements by column
        return [sum(col) / len(matrix) for col in zip(*matrix)]
    elif mode == "row":
        return [sum(row) / len(row) for row in matrix]
    else:
        raise ValueError("Mode must be 'row' or 'column'")


print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode="column"))
print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode="column"))
