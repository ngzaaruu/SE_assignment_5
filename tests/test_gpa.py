import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gpa import calculate_gpa, letter_to_points, score_to_letter  # noqa: E402


def test_score_to_letter_boundaries():
    assert score_to_letter(100) == "A"
    assert score_to_letter(95) == "A"
    assert score_to_letter(94) == "A-"
    assert score_to_letter(49) == "F"


def test_letter_to_points():
    assert letter_to_points("A") == 4.0
    assert letter_to_points("B") == 3.0
    assert letter_to_points("F") == 0.0


def test_calculate_gpa_weighted_by_credits():
    courses = [
        {"name": "Math", "credits": 5, "score": 96},  # A  -> 4.0
        {"name": "History", "credits": 3, "score": 81},  # B -> 3.0
    ]
    # (4.0*5 + 3.0*3) / 8 = 3.625 -> 3.62
    assert calculate_gpa(courses) == 3.62
