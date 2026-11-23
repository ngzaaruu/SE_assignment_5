"""Core GPA calculation logic (4.0 scale, KBTU-style letter grades)."""


def score_to_letter(score):
    if score >= 95:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 85:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 75:
        return "B-"
    elif score >= 70:
        return "C+"
    elif score >= 65:
        return "C"
    elif score >= 60:
        return "C-"
    elif score >= 55:
        return "D+"
    elif score >= 50:
        return "D"
    else:
        return "F"


def letter_to_points(letter):
    if letter == "A":
        return 4.0
    elif letter == "A-":
        return 3.67
    elif letter == "B+":
        return 3.33
    elif letter == "B":
        return 3.0
    elif letter == "B-":
        return 2.67
    elif letter == "C+":
        return 2.33
    elif letter == "C":
        return 2.0
    elif letter == "C-":
        return 1.67
    elif letter == "D+":
        return 1.33
    elif letter == "D":
        return 1.0
    else:
        return 0.0


def calculate_gpa(courses):
    """courses: list of dicts {"name": str, "credits": int, "score": float}"""
    total_points = 0
    total_credits = 0
    for c in courses:
        letter = score_to_letter(c["score"])
        points = letter_to_points(letter)
        total_points += points * c["credits"]
        total_credits += c["credits"]
    return round(total_points / total_credits, 2)
