# Student Performance Analyzer — Project Report

## 1. Introduction
The Student Performance Analyzer is a Python 3 project that reads student marks from a CSV dataset and analyses academic performance in Maths, Physics and Chemistry.

## 2. Problem statement
The program calculates each student's total marks, percentage and grade. It also calculates class mean, median and standard deviation, identifies the topper, calculates subject-wise averages, and displays charts.

## 3. Tools and technologies
- Python 3
- Pandas: reading and organizing CSV data
- NumPy: subject-wise average calculations
- Statistics: mean, median and population standard deviation
- Matplotlib: bar chart and histogram

## 4. Input format
The CSV file must contain these column headings:
`Name,Maths,Physics,Chemistry`

Each subject mark must be numeric and between 0 and 100.

## 5. Grade criteria
| Percentage | Grade |
|---|---|
| 90 and above | A |
| 75 to less than 90 | B |
| 60 to less than 75 | C |
| 40 to less than 60 | D |
| Below 40 | F |

Percentage = (Maths + Physics + Chemistry) / 3.

## 6. Algorithm
1. Read `students.csv` using Pandas.
2. Check that all required columns exist.
3. Validate each student's name and marks.
4. Skip a row if a mark is missing, non-numeric, non-finite or outside 0–100.
5. Calculate total, percentage and grade for each valid student.
6. If menu option 1 is selected, display student results.
7. If menu option 2 is selected, calculate class statistics and topper.
8. Calculate subject averages using NumPy.
9. Display a bar chart and a histogram using Matplotlib.

## 7. Test cases
### Test Case 1: Normal input
Aman (80,70,90), Riya (60,65,70), Karan (40,35,50).
Expected results:
- Aman | 240 | 80.00% | B
- Riya | 195 | 65.00% | C
- Karan | 125 | 41.67% | D

### Test Case 2: Boundary/minimum input
Neha (100,100,100), Ravi (0,0,0).
Expected results:
- Neha | 300 | 100.00% | A
- Ravi | 0 | 0.00% | F

### Test Case 3: Invalid input
Amit (85,abc,70).
Expected message:
`Invalid marks for Amit in Physics: 'abc'. Row skipped.`

### Test Case 4: Statistics
Using the same data as Test Case 1:
- Mean %: 62.22
- Median %: 65.00
- Standard deviation: 15.77
- Topper: Aman (80.00%)
- Maths average: 60.00
- Physics average: 56.67
- Chemistry average: 70.00
- Bar chart and histogram are displayed.

## 8. How to execute
1. Install Python 3.
2. Open the project folder in VS Code.
3. Run `python -m pip install -r requirements.txt`.
4. Run `python student_analyzer.py`.
5. Enter 1 or 2 when prompted.

## 9. Conclusion
The project automates basic student-mark analysis, handles invalid records, summarizes class performance and presents the results visually.
