import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from analysis import load_data, analyze_result, subject_pass_fail

from charts import (
    show_subject_chart,
    show_pass_fail_chart,
    show_top_students_chart,
    show_marks_distribution_chart
)


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("Student Result Analyzer")
root.geometry("1100x700")
root.minsize(900, 600)


# ==========================================
# STYLING
# ==========================================

style = ttk.Style()

try:
    style.theme_use("clam")
except tk.TclError:
    pass

style.configure(
    "Treeview",
    rowheight=30,
    font=("Arial", 10)
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold")
)

style.configure(
    "TButton",
    font=("Arial", 10)
)


# ==========================================
# HEADING
# ==========================================

heading = tk.Label(
    root,
    text="Student Result Analyzer",
    font=("Arial", 24, "bold")
)

heading.pack(pady=(15, 10))


# ==========================================
# FILE SELECTION
# ==========================================

file_frame = tk.Frame(root)
file_frame.pack(pady=5)

browse_button = tk.Button(
    file_frame,
    text="Select CSV File",
    width=18,
    command=lambda: select_file()
)

browse_button.pack(side="left", padx=5)

load_button = tk.Button(
    file_frame,
    text="Analyze Result",
    width=18,
    command=lambda: analyze(),
    state="disabled"
)

load_button.pack(side="left", padx=5)


# ==========================================
# SELECTED FILE LABEL
# ==========================================

file_label = tk.Label(
    root,
    text="No file selected",
    font=("Arial", 10)
)

file_label.pack(pady=5)


# ==========================================
# SEARCH FRAME
# ==========================================

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(
    search_frame,
    text="Search Student:",
    font=("Arial", 11)
)

search_label.pack(side="left", padx=5)

search_entry = tk.Entry(
    search_frame,
    width=25,
    font=("Arial", 11)
)

search_entry.pack(side="left", padx=5)

search_button = tk.Button(
    search_frame,
    text="Search",
    width=12,
    command=lambda: search_student()
)

search_button.pack(side="left", padx=5)

show_all_button = tk.Button(
    search_frame,
    text="Show All",
    width=12,
    command=lambda: show_all_students()
)

show_all_button.pack(side="left", padx=5)


# ==========================================
# SUMMARY FRAME
# ==========================================

summary_frame = tk.Frame(root)
summary_frame.pack(pady=10)

average_label = tk.Label(
    summary_frame,
    text="Class Average: -",
    font=("Arial", 12, "bold"),
    width=22
)

average_label.grid(row=0, column=0, padx=5)

highest_label = tk.Label(
    summary_frame,
    text="Highest: -",
    font=("Arial", 12, "bold"),
    width=22
)

highest_label.grid(row=0, column=1, padx=5)

pass_label = tk.Label(
    summary_frame,
    text="Pass: -",
    font=("Arial", 12, "bold"),
    width=15,
    fg="green"
)

pass_label.grid(row=0, column=2, padx=5)

fail_label = tk.Label(
    summary_frame,
    text="Fail: -",
    font=("Arial", 12, "bold"),
    width=15,
    fg="red"
)

fail_label.grid(row=0, column=3, padx=5)


# ==========================================
# TABLE FRAME
# ==========================================

table_frame = tk.Frame(root)

table_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)


# ==========================================
# TREEVIEW TABLE
# ==========================================

columns = ()

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

# PASS = GREEN
tree.tag_configure(
    "pass",
    background="lightgreen",
    foreground="black"
)

# FAIL = RED
tree.tag_configure(
    "fail",
    background="lightcoral",
    foreground="black"
)


# Vertical scrollbar
vertical_scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(
    yscrollcommand=vertical_scrollbar.set
)


# Horizontal scrollbar
horizontal_scrollbar = ttk.Scrollbar(
    table_frame,
    orient="horizontal",
    command=tree.xview
)

tree.configure(
    xscrollcommand=horizontal_scrollbar.set
)


tree.grid(
    row=0,
    column=0,
    sticky="nsew"
)

vertical_scrollbar.grid(
    row=0,
    column=1,
    sticky="ns"
)

horizontal_scrollbar.grid(
    row=1,
    column=0,
    sticky="ew"
)

table_frame.grid_rowconfigure(
    0,
    weight=1
)

table_frame.grid_columnconfigure(
    0,
    weight=1
)


# ==========================================
# SUBJECT ANALYSIS FRAME
# ==========================================

subject_frame = tk.Frame(root)
subject_frame.pack(pady=10)

subject_label = tk.Label(
    subject_frame,
    text="Select Subject:",
    font=("Arial", 11)
)

subject_label.pack(side="left", padx=5)

subject_var = tk.StringVar()

subject_dropdown = ttk.Combobox(
    subject_frame,
    textvariable=subject_var,
    values=[],
    state="readonly",
    width=12
)

subject_dropdown.pack(side="left", padx=5)


# Subject Analysis
subject_button = tk.Button(
    subject_frame,
    text="Subject Analysis",
    width=15,
    command=lambda: subject_analysis()
)

subject_button.pack(side="left", padx=3)


# Subject Chart
chart_button = tk.Button(
    subject_frame,
    text="Show Chart",
    width=12,
    command=lambda: show_chart()
)

chart_button.pack(side="left", padx=3)


# Pass/Fail Chart
pass_fail_button = tk.Button(
    subject_frame,
    text="Pass/Fail Chart",
    width=13,
    command=lambda: show_pass_fail()
)

pass_fail_button.pack(side="left", padx=3)


# Top Students
top_students_button = tk.Button(
    subject_frame,
    text="Top 10 Students",
    width=14,
    command=lambda: show_top_students()
)

top_students_button.pack(side="left", padx=3)


# Marks Distribution
marks_distribution_button = tk.Button(
    subject_frame,
    text="Marks Distribution",
    width=17,
    command=lambda: show_marks_distribution()
)

marks_distribution_button.pack(side="left", padx=3)


# Subject Pass/Fail
subject_pass_fail_button = tk.Button(
    subject_frame,
    text="Subject Pass/Fail",
    width=16,
    command=lambda: show_subject_pass_fail()
)

subject_pass_fail_button.pack(side="left", padx=3)


# Export CSV
export_button = tk.Button(
    subject_frame,
    text="Export CSV",
    width=12,
    command=lambda: export_result()
)

export_button.pack(side="left", padx=3)


# Reset
reset_button = tk.Button(
    subject_frame,
    text="Reset",
    width=10,
    command=lambda: reset_project()
)

reset_button.pack(side="left", padx=3)


# ==========================================
# SELECT CSV FILE FUNCTION
# ==========================================

def select_file():

    file_path = filedialog.askopenfilename(
        title="Select Student CSV File",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("All Files", "*.*")
        ]
    )

    if file_path:

        file_label.config(
            text=file_path
        )

        root.selected_file = file_path

        load_button.config(
            state="normal"
        )


# ==========================================
# DISPLAY TABLE FUNCTION
# ==========================================

def display_table(df):

    # Remove previous rows
    for item in tree.get_children():
        tree.delete(item)

    # Set columns
    tree["columns"] = columns
    tree["show"] = "headings"

    # Configure column headings
    for column in columns:

        tree.heading(
            column,
            text=column
        )

        if column == "Name":

            tree.column(
                column,
                width=160,
                anchor="center"
            )

        elif column == "Percentage":

            tree.column(
                column,
                width=110,
                anchor="center"
            )

        elif column == "Grade":

            tree.column(
                column,
                width=80,
                anchor="center"
            )

        else:

            tree.column(
                column,
                width=100,
                anchor="center"
            )

    # Insert student rows
    for index, row in df.iterrows():

        values = []

        for column in columns:

            value = (
                row[column]
                if column in row.index
                else ""
            )

            # Format percentage
            if column == "Percentage":
                value = f"{value:.2f}"

            values.append(value)

        # Apply color based on Status
        status = str(
            row.get("Status", "")
        ).strip().lower()

        if status == "pass":

            tag = "pass"

        else:

            tag = "fail"

        # Insert row with tag
        tree.insert(
            "",
            "end",
            values=values,
            tags=(tag,)
        )


# ==========================================
# ANALYZE FUNCTION
# ==========================================

def analyze():

    global columns

    try:

        if not hasattr(root, "selected_file"):

            messagebox.showwarning(
                "Warning",
                "Please select a CSV file first."
            )

            return

        # Load CSV
        df = load_data(
            root.selected_file
        )

        # Analyze results
        df = analyze_result(df)

        # Get subject names
        subjects = df.attrs.get(
            "subjects",
            []
        )

        # Update subject dropdown
        subject_dropdown["values"] = subjects

        if subjects:
            subject_dropdown.current(0)

        # Set table columns
        columns = (
            ["Name"]
            + subjects
            + ["Total", "Percentage", "Status", "Grade"]
        )

        # Store analyzed data
        root.df = df

        # Calculate class average
        average = df["Percentage"].mean()

        # Find highest scorer
        highest = df.loc[
            df["Percentage"].idxmax()
        ]

        # Count pass and fail students
        pass_count = (
            df["Status"]
            .astype(str)
            .str.strip()
            .str.lower()
            .eq("pass")
            .sum()
        )

        fail_count = (
            df["Status"]
            .astype(str)
            .str.strip()
            .str.lower()
            .eq("fail")
            .sum()
        )

        # Update summary labels
        average_label.config(
            text=f"Class Average: {average:.2f}%"
        )

        highest_label.config(
            text=f"Highest: {highest['Name']}"
        )

        pass_label.config(
            text=f"Pass: {pass_count}"
        )

        fail_label.config(
            text=f"Fail: {fail_count}"
        )

        # Display table with colors
        display_table(df)

        messagebox.showinfo(
            "Success",
            "Result analyzed successfully!"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# ==========================================
# SEARCH STUDENT FUNCTION
# ==========================================

def search_student():

    name = search_entry.get().strip()

    if name == "":

        messagebox.showwarning(
            "Warning",
            "Please enter a student name."
        )

        return

    if not hasattr(root, "df"):

        messagebox.showwarning(
            "Warning",
            "Please analyze a CSV file first."
        )

        return

    df = root.df

    # Case-insensitive partial search
    filtered_df = df[
        df["Name"]
        .astype(str)
        .str.strip()
        .str.contains(
            name,
            case=False,
            na=False,
            regex=False
        )
    ]

    if filtered_df.empty:

        messagebox.showinfo(
            "Result",
            "Student not found."
        )

        return

    # Display matching students with colors
    display_table(filtered_df)


# ==========================================
# SHOW ALL STUDENTS FUNCTION
# ==========================================

def show_all_students():

    if not hasattr(root, "df"):

        messagebox.showwarning(
            "Warning",
            "Please analyze a CSV file first."
        )

        return

    display_table(root.df)


# ==========================================
# RESET FUNCTION
# ==========================================

def reset_project():

    # Clear table
    for item in tree.get_children():
        tree.delete(item)

    # Clear search
    search_entry.delete(
        0,
        tk.END
    )

    # Reset summary labels
    average_label.config(
        text="Class Average: -"
    )

    highest_label.config(
        text="Highest: -"
    )

    pass_label.config(
        text="Pass: -"
    )

    fail_label.config(
        text="Fail: -"
    )

    # Reset file label
    file_label.config(
        text="No file selected"
    )

    # Disable analyze button
    load_button.config(
        state="disabled"
    )

    # Clear subject dropdown
    subject_dropdown.set("")
    subject_dropdown["values"] = []

    # Remove stored data
    if hasattr(root, "df"):
        del root.df

    if hasattr(root, "selected_file"):
        del root.selected_file


# ==========================================
# SUBJECT ANALYSIS FUNCTION
# ==========================================

def subject_analysis():

    if not hasattr(root, "df"):

        messagebox.showwarning(
            "Warning",
            "Please analyze a CSV file first."
        )

        return

    subject = subject_var.get()

    if subject == "":

        messagebox.showwarning(
            "Warning",
            "Please select a subject first."
        )

        return

    df = root.df

    if subject not in df.columns:

        messagebox.showerror(
            "Error",
            f"{subject} is not available."
        )

        return

    # Convert marks to numeric values
    marks = df[subject]

    # Remove missing marks for calculations
    valid_marks = marks.dropna()

    if valid_marks.empty:

        messagebox.showwarning(
            "Warning",
            "No valid marks are available for this subject."
        )

        return

    # Calculate average
    average = valid_marks.mean()

    # Highest and lowest marks
    highest_index = valid_marks.idxmax()
    lowest_index = valid_marks.idxmin()

    highest_name = df.loc[
        highest_index,
        "Name"
    ]

    highest_marks = df.loc[
        highest_index,
        subject
    ]

    lowest_name = df.loc[
        lowest_index,
        "Name"
    ]

    lowest_marks = df.loc[
        lowest_index,
        subject
    ]

    # Show result
    messagebox.showinfo(
        "Subject Analysis",

        f"Subject: {subject}\n\n"
        f"Average Marks: {average:.2f}\n"
        f"Highest Scorer: {highest_name} ({highest_marks})\n"
        f"Lowest Scorer: {lowest_name} ({lowest_marks})"
    )


# ==========================================
# SHOW SUBJECT CHART
# ==========================================

def show_chart():

    if not hasattr(root, "df"):

        messagebox.showwarning(
            "Warning",
            "Please analyze a CSV file first."
        )

        return

    show_subject_chart(root.df)


# ==========================================
# SHOW PASS/FAIL CHART
# ==========================================

def show_pass_fail():

    if not hasattr(root, "df"):

        messagebox.showwarning(
            "Warning",
            "Please analyze a CSV file first."
        )

        return

    show_pass_fail_chart(root.df)


# ==========================================
# SHOW TOP 10 STUDENTS
# ==========================================

def show_top_students():

    if not hasattr(root, "df"):

        messagebox.showwarning(
            "Warning",
            "Please analyze a CSV file first."
        )

        return

    show_top_students_chart(root.df)


# ==========================================
# SHOW MARKS DISTRIBUTION
# ==========================================

def show_marks_distribution():

    if not hasattr(root, "df"):

        messagebox.showwarning(
            "Warning",
            "Please analyze a CSV file first."
        )

        return

    show_marks_distribution_chart(root.df)


# ==========================================
# EXPORT RESULT FUNCTION
# ==========================================

def export_result():

    if not hasattr(root, "df"):

        messagebox.showwarning(
            "Warning",
            "Please analyze a CSV file first."
        )

        return

    file_path = filedialog.asksaveasfilename(
        title="Export Student Results",
        defaultextension=".csv",
        filetypes=[
            ("CSV Files", "*.csv")
        ]
    )

    if file_path:

        try:

            root.df.to_csv(
                file_path,
                index=False
            )

            messagebox.showinfo(
                "Success",
                "Result exported successfully!"
            )

        except Exception as error:

            messagebox.showerror(
                "Export Error",
                str(error)
            )


# ==========================================
# SUBJECT-WISE PASS/FAIL FUNCTION
# ==========================================

def show_subject_pass_fail():

    if not hasattr(root, "df"):

        messagebox.showwarning(
            "Warning",
            "Please analyze a CSV file first."
        )

        return

    subject = subject_var.get()

    if subject == "":

        messagebox.showwarning(
            "Warning",
            "Please select a subject."
        )

        return

    df = root.df

    if subject not in df.columns:

        messagebox.showerror(
            "Error",
            f"{subject} column not found."
        )

        return

    # Convert marks to numeric values
    marks = df[subject]

    valid_marks = marks.dropna()

    if valid_marks.empty:

        messagebox.showwarning(
            "Warning",
            "No valid marks are available for this subject."
        )

        return

    # Pass and fail counts
    pass_count = (
        valid_marks >= 33
    ).sum()

    fail_count = (
        valid_marks < 33
    ).sum()

    total_students = len(valid_marks)

    pass_percentage = (
        pass_count / total_students
    ) * 100

    result = (
        f"Subject: {subject}\n\n"
        f"Students with valid marks: {total_students}\n"
        f"Passed Students: {pass_count}\n"
        f"Failed Students: {fail_count}\n"
        f"Pass Percentage: {pass_percentage:.2f}%"
    )

    messagebox.showinfo(
        "Subject Pass/Fail Result",
        result
    )


# ==========================================
# START APPLICATION
# ==========================================

root.mainloop()