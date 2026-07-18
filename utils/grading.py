
GRADE_POINTS = {
    "A+": 4.00,
    "A": 3.75,
    "B+": 3.50,
    "B": 3.25,
    "C+": 3.00,
    "C": 2.75,
    "D+": 2.50,
    "D": 2.25,
    "F": 0.00,
}

GRADE_RANGES = {
    "A+": (90, 100),
    "A": (85, 89.99),
    "B+": (80, 84.99),
    "B": (75, 79.99),
    "C+": (70, 74.99),
    "C": (65, 69.99),
    "D+": (60, 64.99),
    "D": (50, 59.99),
    "F": (0, 49.99),
}
def get_letter_grade(mark):
    """
    Returns the letter grade based on marks.
    """

    for grade, (minimum, maximum) in GRADE_RANGES.items():
        if minimum <= mark <= maximum:
            return grade

    return None


def get_grade_point(mark):
    """
    Returns the grade point based on marks.
    """

    letter = get_letter_grade(mark)

    if letter is None:
        return None

    return GRADE_POINTS[letter]