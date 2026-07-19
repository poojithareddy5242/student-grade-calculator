def calculate_grade(percentage):
    if percentage >= 95:
        return "Distinction"
    elif percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"

def main():
    print("=== Student Grade Calculator ===")
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    total_marks = 0
    max_marks = num_subjects * 100
    subject_marks = []

    for i in range(1, num_subjects + 1):
        marks = float(input(f"Enter marks for Subject {i} (out of 100): "))
        subject_marks.append(marks)
        total_marks += marks

        if marks < 40:
            print(f"⚠️  Warning: Failed in Subject {i}")

    percentage = (total_marks / max_marks) * 100
    grade = calculate_grade(percentage)

    print("\n--- Result ---")
    print(f"Name: {name}")
    print(f"Subject-wise Marks: {subject_marks}")
    print(f"Total Marks: {total_marks}/{max_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()

main()
