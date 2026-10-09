def calculate_average(grades: list[int]) -> float:
    if not grades:
        raise ValueError("Список оценок пуст")
    return round(sum(grades) / len(grades), 2)


def grade_bounds(grades: list[int]) -> tuple[int, int]:
    if not grades:
        raise ValueError("Список оценок пуст")
    return min(grades), max(grades)
