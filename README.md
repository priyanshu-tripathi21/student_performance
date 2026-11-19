# Student Performance Analyzer

## Project details
- Language: Python 3
- Libraries: Pandas, NumPy, Matplotlib, Statistics
- Input: `students.csv`
- Main program: `student_analyzer.py`

## Features
1. Reads student marks from a CSV file using Pandas.
2. Validates marks and skips invalid student rows.
3. Calculates total marks, percentage and grade.
4. Displays mean, median and population standard deviation.
5. Finds the topper and subject-wise averages.
6. Displays a subject-average bar chart and percentage histogram.

## Grade criteria
- 90% and above: A
- 75% to less than 90%: B
- 60% to less than 75%: C
- 40% to less than 60%: D
- Below 40%: F

Each subject is out of 100. Percentage = (Maths + Physics + Chemistry) / 3.

## Setup in VS Code
1. Install Python 3.
2. Open this project folder in VS Code.
3. Open Terminal > New Terminal.
4. Install dependencies:
   `python -m pip install -r requirements.txt`
5. Run:
   `python student_analyzer.py`
6. Enter 1 for student results or 2 for class statistics.

## Running the four supplied test cases
The sample files are in `test_cases/`.
Copy the required test CSV into the project folder and rename it `students.csv`,
replacing the previous `students.csv`, then run the program.

- `case1_normal.csv`: normal input; choose menu option 1.
- `case2_boundary.csv`: minimum and maximum marks; choose option 1.
- `case3_invalid.csv`: invalid Physics mark; choose option 1.
- `case4_statistics.csv`: same data as case 1; choose option 2.

## Expected statistics for Test Case 4
- Mean %: 62.22
- Median %: 65.00
- Std Dev: 15.77
- Topper: Aman (80.00%)
- Maths average: 60.00
- Physics average: 56.67
- Chemistry average: 70.00

The standard deviation is the population standard deviation, matching the supplied expected output.
