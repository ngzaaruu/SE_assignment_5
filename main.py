"""Console entry point for the GPA calculator."""
import json

from gpa import calculate_gpa, score_to_letter, validate_course

DATA_FILE = "courses.json"


def load_courses():
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_courses(courses):
    with open(DATA_FILE, "w") as f:
        json.dump(courses, f, indent=2)


def main():
    courses = load_courses()
    while True:
        print("\n1) Add course  2) List courses  3) Show GPA  4) Exit")
        choice = input("> ")
        if choice == "1":
            name = input("Course name: ")
            try:
                credits = int(input("Credits: "))
                score = float(input("Score (0-100): "))
                validate_course(score, credits)
            except ValueError as e:
                print("Not added:", e)
                continue
            courses.append({"name": name, "credits": credits, "score": score})
            save_courses(courses)
            print("Added.")
        elif choice == "2":
            for c in courses:
                print(f"{c['name']}: {c['score']} ({score_to_letter(c['score'])}), {c['credits']} cr")
        elif choice == "3":
            try:
                print("GPA:", calculate_gpa(courses))
            except ValueError as e:
                print(e)
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
