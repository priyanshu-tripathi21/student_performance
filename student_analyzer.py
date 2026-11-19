import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

SUBJECTS = ["Maths", "Physics", "Chemistry"]


def load_and_validate_data(filename="students.csv"):
    """Load student records and skip rows containing invalid marks."""
    try:
        df = pd.read_csv(filename, dtype=str, keep_default_na=False)
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        return pd.DataFrame()
    except Exception as error:
        print(f"Error reading CSV file: {error}")
        return pd.DataFrame()

    required_columns = ["Name"] + SUBJECTS
    missing_columns = [column for column in required_columns
                       if column not in df.columns]

    if missing_columns:
        print("CSV file is missing these columns:",
              ", ".join(missing_columns))
        return pd.DataFrame()

    valid_records = []

    for _, row in df.iterrows():
        name = row["Name"].strip()
        marks = {}
        row_is_valid = True

        for subject in SUBJECTS:
            raw_mark = row[subject].strip()

            try:
                mark = float(raw_mark)
                if not np.isfinite(mark) or not 0 <= mark <= 100:
                    raise ValueError
                marks[subject] = mark
            except ValueError:
                print(
                    f"Invalid marks for {name} in {subject}: "
                    f"'{raw_mark}'. Row skipped."
                )
                row_is_valid = False
                break

        if not name:
            print("Invalid student name. Row skipped.")
            row_is_valid = False

        if row_is_valid:
            total = sum(marks.values())
            percentage = total / len(SUBJECTS)

            if percentage >= 90:
                grade = "A"
            elif percentage >= 75:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 40:
                grade = "D"
            else:
                grade = "F"

            record = {
                "Name": name,
                **marks,
                "Total": total,
                "Percentage": percentage,
                "Grade": grade
            }
            valid_records.append(record)

    return pd.DataFrame(valid_records)


def display_student_results(data):
    """Display each valid student's total, percentage and grade."""
    if data.empty:
        print("No valid student records found.")
        return

    print("\nName | Total | Percentage | Grade")
    for _, student in data.iterrows():
        print(
            f"{student['Name']} | "
            f"{student['Total']:.0f} | "
            f"{student['Percentage']:.2f}% | "
            f"{student['Grade']}"
        )


def display_class_statistics(data):
    """Display class statistics, topper, subject averages and charts."""
    if data.empty:
        print("No valid student records found.")
        return

    percentages = data["Percentage"].tolist()

    # Statistics module: mean, median and population standard deviation
    mean_percentage = statistics.mean(percentages)
    median_percentage = statistics.median(percentages)
    std_deviation = statistics.pstdev(percentages)

    # Find the student with the highest percentage
    topper = data.loc[data["Percentage"].idxmax()]

    print("\n===== CLASS STATISTICS =====")
    print(f"Mean %: {mean_percentage:.2f}")
    print(f"Median %: {median_percentage:.2f}")
    print(f"Std Dev: {std_deviation:.2f}")
    print(
        f"Topper: {topper['Name']} "
        f"({topper['Percentage']:.2f}%)"
    )

    # NumPy: calculate subject-wise averages
    subject_averages = np.mean(data[SUBJECTS].to_numpy(dtype=float), axis=0)

    print("\nSubject averages:")
    for subject, average in zip(SUBJECTS, subject_averages):
        print(f"{subject}: {average:.2f}")

    # Bar chart: subject-wise average marks
    plt.figure(figsize=(8, 5))
    plt.bar(SUBJECTS, subject_averages)
    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

    # Histogram: distribution of student percentages
    plt.figure(figsize=(8, 5))
    plt.hist(percentages, bins=5, edgecolor="black")
    plt.title("Student Percentage Distribution")
    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.show()


def main():
    print("===== STUDENT PERFORMANCE ANALYZER =====")

    data = load_and_validate_data()

    if data.empty:
        print("There are no valid records to analyse.")
        return

    print("\n1. Display Student Results")
    print("2. Display Class Statistics")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        display_student_results(data)
    elif choice == "2":
        display_class_statistics(data)
    else:
        print("Invalid menu choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
