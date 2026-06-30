import os
import matplotlib.pyplot as plt

def visualize_data(df):


    os.makedirs("visualize", exist_ok=True) 

    # Grade Distribution - (bar graph)
    grade_counts = df["Grades"].value_counts()

    plt.figure(figsize=(6,4))  #size of figure
    plt.bar(grade_counts.index, grade_counts.values)

    plt.title("Grade Distribution")
    plt.xlabel("Grades")
    plt.ylabel("Students")

    plt.savefig("visualize/grade_distribution.png")
    plt.show()
    plt.close()

    # Pass vs Fail - (pie chart)
    result = df["Result"].value_counts()

    plt.figure(figsize=(6,6))
    plt.pie(result.values, labels=result.index, autopct="%1.1f%%")
    plt.title("Pass vs Fail")

    plt.savefig("visualize/pass_vs_fail.png")
    plt.show()
    plt.close()

    # Attendance Distribution - (histogram)
    plt.figure(figsize=(7,4))
    plt.hist(df["Attendance"], bins=10)

    plt.title("Attendance Distribution")
    plt.xlabel("Attendance")
    plt.ylabel("Students")

    plt.savefig("visualize/attendance_distribution.png")
    plt.show()
    plt.close()

    # Average Marks by Grade
    avg_marks = df.groupby("Grades")["Marks"].mean()

    plt.figure(figsize=(6,4))
    plt.bar(avg_marks.index, avg_marks.values)

    plt.title("Average Marks by Grade")
    plt.xlabel("Grades")
    plt.ylabel("Average Marks")

    plt.savefig("visualize/average_marks_by_grade.png")
    plt.show()
    plt.close()

    print("Charts saved successfully in 'visualize' folder.")