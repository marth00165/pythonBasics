import pandas as pd
import numpy as np

students = np.array(["Robert", "Mary", "Jane", "Frank"])

print(students)

midterm_grades = [82, 76, 69, 96]
final_grades = [90, 84, 70, 65]


midterm_grades_series = pd.Series(midterm_grades, index=students)
final_grades_series = pd.Series(final_grades, index=students)

print(midterm_grades_series, "Midterms")
print(final_grades_series, "Finals")
