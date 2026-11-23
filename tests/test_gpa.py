import sys
from pathlib import Path

import pytest

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


def test_custom_grading_scale():
    from gpa import GradingScale

    pass_fail = GradingScale(name="Pass/Fail", bands=((50, "P", 4.0), (0, "F", 0.0)))
    courses = [
        {"name": "Art", "credits": 2, "score": 60},  # P -> 4.0
        {"name": "Music", "credits": 2, "score": 40},  # F -> 0.0
    ]
    assert calculate_gpa(courses, pass_fail) == 2.0


# --- Task 07: tests for risks R1 and R2 ---
def test_empty_courses_gives_clear_error():  # R1
    with pytest.raises(ValueError, match="No courses"):
        calculate_gpa([])


@pytest.mark.parametrize("bad_score", [150, -5, float("inf"), float("nan")])
def test_invalid_score_is_rejected(bad_score):  # R2
    with pytest.raises(ValueError, match="Score"):
        calculate_gpa([{"name": "X", "credits": 3, "score": bad_score}])


@pytest.mark.parametrize("bad_credits", [0, -3])
def test_invalid_credits_are_rejected(bad_credits):  # R2
    with pytest.raises(ValueError, match="Credits"):
        calculate_gpa([{"name": "X", "credits": bad_credits, "score": 90}])
