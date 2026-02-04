
ISENTION_LIMIT = 2000.0
LOW_TAX = 0.10
HIGH_TAX = 0.20


def calc_salary(value: float) -> float:
    if value < ISENTION_LIMIT :
        return value-(value * LOW_TAX)
    else:
        return value-(value * HIGH_TAX)

