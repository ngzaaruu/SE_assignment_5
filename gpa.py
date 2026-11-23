"""Core GPA calculation logic.

The grading scale is a Strategy: a GradingScale object holds the bands
(min score -> letter -> points). calculate_gpa() uses whatever scale it is
given, so a new scale can be added without changing the calculation code.
"""
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class GradingScale:
    name: str
    # (min_score, letter, points), ordered from highest to lowest
    bands: tuple[tuple[float, str, float], ...]

    def letter(self, score: float) -> str:
        for min_score, letter, _ in self.bands:
            if score >= min_score:
                return letter
        return self.bands[-1][1]

    def points(self, letter: str) -> float:
        for _, band_letter, points in self.bands:
            if band_letter == letter:
                return points
        return 0.0


KBTU_SCALE = GradingScale(
    name="KBTU 4.0",
    bands=(
        (95, "A", 4.0),
        (90, "A-", 3.67),
        (85, "B+", 3.33),
        (80, "B", 3.0),
        (75, "B-", 2.67),
        (70, "C+", 2.33),
        (65, "C", 2.0),
        (60, "C-", 1.67),
        (55, "D+", 1.33),
        (50, "D", 1.0),
        (0, "F", 0.0),
    ),
)


def score_to_letter(score: float, scale: GradingScale = KBTU_SCALE) -> str:
    return scale.letter(score)


def letter_to_points(letter: str, scale: GradingScale = KBTU_SCALE) -> float:
    return scale.points(letter)


def validate_course(score: float, credits: int) -> None:
    """Raise ValueError if a score or credits value is not allowed (risk R2)."""
    if not math.isfinite(score) or not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    if type(credits) is not int or credits <= 0:
        raise ValueError("Credits must be a whole number greater than 0.")


def calculate_gpa(courses: list[dict], scale: GradingScale = KBTU_SCALE) -> float:
    """courses: list of dicts {"name": str, "credits": int, "score": float}"""
    if not courses:
        raise ValueError("No courses yet. Add a course first.")  # risk R1
    total_points = 0.0
    total_credits = 0
    for c in courses:
        validate_course(c["score"], c["credits"])
        points = scale.points(scale.letter(c["score"]))
        total_points += points * c["credits"]
        total_credits += c["credits"]
    return round(total_points / total_credits, 2)
