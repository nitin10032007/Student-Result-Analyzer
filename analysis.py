import pandas as pd
import numpy as np


def load_data(file_path):
    df = pd.read_csv(file_path)

    # Name column compulsory hai
    if "Name" not in df.columns:
        raise ValueError("CSV must contain a Name column")

    # Calculated columns ko subjects nahi maana jayega
    calculated_columns = [
        "Total",
        "Percentage",
        "Status",
        "Grade"
    ]

    # Automatically subjects detect honge
    subjects = [
        column for column in df.columns
        if column != "Name" and column not in calculated_columns
    ]

    if len(subjects) == 0:
        raise ValueError("No subject columns found in CSV")

    # Subject marks ko numeric mein convert karna
    for subject in subjects:
        df[subject] = pd.to_numeric(
            df[subject],
            errors="coerce"
        )

    # Missing marks ko 0 se replace karna
    df[subjects] = df[subjects].fillna(0)

    return df


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def analyze_result(df):
    calculated_columns = [
        "Total",
        "Percentage",
        "Status",
        "Grade"
    ]

    subjects = [
        column for column in df.columns
        if column != "Name" and column not in calculated_columns
    ]

    # Total marks of all subjects
    df["Total"] = df[subjects].sum(axis=1)

    # Har subject 100 marks ka assume kiya gaya hai
    maximum_marks = len(subjects) * 100

    df["Percentage"] = (
        df["Total"] / maximum_marks * 100
    ).round(2)

    # Har subject mein minimum 33 marks
    df["Status"] = np.where(
        df[subjects].ge(33).all(axis=1),
        "Pass",
        "Fail"
    )

    # Grade calculate
    df["Grade"] = df["Percentage"].apply(calculate_grade)

    # Subjects ko future use ke liye save karna
    df.attrs["subjects"] = subjects

    return df


def subject_pass_fail(df):
    subjects = df.attrs.get("subjects", [])

    result = []

    for subject in subjects:
        pass_count = (df[subject] >= 33).sum()
        fail_count = (df[subject] < 33).sum()

        result.append({
            "Subject": subject,
            "Pass": pass_count,
            "Fail": fail_count
        })

    return pd.DataFrame(result)