def calculate_average(grades):
    if not grades:
        raise ValueError("Список оценок пуст")
    return round(sum(grades) / len(grades), 2)


def grade_bounds(grades):
    if not grades:
        raise ValueError("Список оценок пуст")
    return min(grades), max(grades)
