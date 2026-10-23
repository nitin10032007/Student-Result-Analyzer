import matplotlib.pyplot as plt


# Show subject-wise average chart
def show_subject_chart(df):

    # Analysis ke time automatically detected subjects
    subjects = df.attrs.get("subjects", [])

    if not subjects:
        raise ValueError("No subjects found")

    # Har subject ka average
    averages = [
        df[subject].mean()
        for subject in subjects
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(subjects, averages)

    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)

    # Average value show karna
    for i, value in enumerate(averages):
        plt.text(
            i,
            value + 1,
            f"{value:.2f}",
            ha="center"
        )

    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


# Show Pass/Fail chart
def show_pass_fail_chart(df):

    if "Status" not in df.columns:
        raise ValueError("Please analyze the result first")

    pass_count = (
        df["Status"] == "Pass"
    ).sum()

    fail_count = (
        df["Status"] == "Fail"
    ).sum()

    labels = ["Pass", "Fail"]
    values = [pass_count, fail_count]

    # Agar data empty ho
    if sum(values) == 0:
        raise ValueError("No result data available")

    plt.figure(figsize=(6, 6))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Pass vs Fail Students")

    plt.tight_layout()
    plt.show()


# Show Top 10 Students chart
def show_top_students_chart(df):

    if "Percentage" not in df.columns:
        raise ValueError("Please analyze the result first")

    top_students = (
        df.sort_values(
            "Percentage",
            ascending=False
        ).head(10)
    )

    if top_students.empty:
        raise ValueError("No student data available")

    plt.figure(figsize=(10, 5))

    plt.bar(
        top_students["Name"],
        top_students["Percentage"]
    )

    plt.title("Top 10 Students")
    plt.xlabel("Student Name")
    plt.ylabel("Percentage")

    plt.ylim(0, 100)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    # Percentage values show karna
    for i, value in enumerate(
        top_students["Percentage"]
    ):
        plt.text(
            i,
            value + 1,
            f"{value:.1f}",
            ha="center"
        )

    plt.tight_layout()
    plt.show()


# Show Marks Distribution Histogram
def show_marks_distribution_chart(df):

    if "Percentage" not in df.columns:
        raise ValueError("Please analyze the result first")

    if df["Percentage"].empty:
        raise ValueError("No marks data available")

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Percentage"],
        bins=10,
        edgecolor="black"
    )

    plt.title("Marks Distribution")
    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")

    plt.xlim(0, 100)

    plt.tight_layout()
    plt.show()