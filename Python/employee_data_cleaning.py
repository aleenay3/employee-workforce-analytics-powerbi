import pandas as pd

# ============================================================
# 1. FILE SETTINGS
# ============================================================

input_file = "Employee_Management_PowerBI.xlsx"
output_file = "cleaned_employees.xlsx"
valid_file = "valid_employees.xlsx"
invalid_file = "invalid_employees.xlsx"
quality_file = "data_quality_report.xlsx"


# ============================================================
# 2. READ EXCEL FILE
# ============================================================

df = pd.read_excel(input_file)

print("Rows before cleaning:", len(df))
print("Columns:", list(df.columns))


# ============================================================
# 3. CHECK REQUIRED COLUMNS
# ============================================================

required_columns = [
    "EmployeeID",
    "EmployeeCode",
    "EmployeeName",
    "Gender",
    "DateOfBirth",
    "Department",
    "Position",
    "Location",
    "JoiningDate",
    "LeavingDate",
    "MonthlySalaryPKR",
    "EmploymentStatus"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )


# ============================================================
# 4. CLEAN TEXT COLUMNS
# ============================================================

text_columns = [
    "EmployeeCode",
    "EmployeeName",
    "Gender",
    "Department",
    "Position",
    "Location",
    "EmploymentStatus"
]

for column in text_columns:
    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )


# ============================================================
# 5. STANDARDIZE GENDER
# ============================================================

df["Gender"] = df["Gender"].str.upper()

df["Gender"] = df["Gender"].replace({
    "M": "MALE",
    "F": "FEMALE"
})

df["Gender"] = df["Gender"].str.title()


# ============================================================
# 6. STANDARDIZE DEPARTMENT
# ============================================================

df["Department"] = df["Department"].str.title()

df["Department"] = df["Department"].replace({
    "It Support": "IT Support"
})


# ============================================================
# 7. STANDARDIZE LOCATION
# ============================================================

df["Location"] = df["Location"].str.title()


# ============================================================
# 8. CONVERT DATE COLUMNS
# ============================================================

date_columns = [
    "DateOfBirth",
    "JoiningDate",
    "LeavingDate"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )


# ============================================================
# 9. CONVERT SALARY TO NUMERIC
# ============================================================

df["MonthlySalaryPKR"] = pd.to_numeric(
    df["MonthlySalaryPKR"],
    errors="coerce"
)


# ============================================================
# 10. DATA QUALITY CHECKS
# ============================================================

print("\nMissing values:")

missing_values = df[required_columns].isnull().sum()

print(missing_values)


# ============================================================
# 11. DUPLICATE CHECK
# ============================================================

duplicate_rows = df.duplicated().sum()

duplicate_employee_ids = (
    df["EmployeeID"].duplicated().sum()
)

print("\nDuplicate rows:", duplicate_rows)
print("Duplicate Employee IDs:", duplicate_employee_ids)


# ============================================================
# 12. REMOVE DUPLICATE ROWS
# ============================================================

df = df.drop_duplicates()


# ============================================================
# 13. INVALID EMPLOYEE ID CHECK
# ============================================================

invalid_employee_ids = df[
    df["EmployeeID"].isna()
]

print(
    "\nInvalid Employee IDs:",
    len(invalid_employee_ids)
)


# ============================================================
# 14. INVALID DATE CHECK
# ============================================================

invalid_dates = df[
    df["LeavingDate"].notna()
    &
    (
        df["LeavingDate"]
        <
        df["JoiningDate"]
    )
]

print(
    "Invalid dates:",
    len(invalid_dates)
)


# ============================================================
# 15. INVALID SALARY CHECK
# ============================================================

invalid_salary = df[
    df["MonthlySalaryPKR"].isna()
    |
    (df["MonthlySalaryPKR"] <= 0)
]

print(
    "Invalid or missing salaries:",
    len(invalid_salary)
)


# ============================================================
# 16. VALIDATE EMPLOYMENT STATUS
# ============================================================

valid_statuses = [
    "Active",
    "Resigned",
    "On Leave",
    "Terminated"
]

invalid_status = df[
    ~df["EmploymentStatus"].isin(valid_statuses)
]

print(
    "Invalid employment statuses:",
    len(invalid_status)
)


# ============================================================
# 17. CREATE VALID / INVALID DATASETS
# ============================================================

valid = df[
    df["EmployeeID"].notna()
    &
    df["JoiningDate"].notna()
    &
    df["EmployeeName"].notna()
    &
    df["MonthlySalaryPKR"].notna()
    &
    (df["MonthlySalaryPKR"] > 0)
    &
    ~(
        df["LeavingDate"].notna()
        &
        (
            df["LeavingDate"]
            <
            df["JoiningDate"]
        )
    )
    &
    df["EmploymentStatus"].isin(valid_statuses)
]

invalid = df.loc[
    ~df.index.isin(valid.index)
]


# ============================================================
# 18. DATA QUALITY SUMMARY
# ============================================================

quality_report = pd.DataFrame({
    "Check": [
        "Rows Before Cleaning",
        "Rows After Cleaning",
        "Missing Values",
        "Duplicate Rows",
        "Duplicate Employee IDs",
        "Invalid Employee IDs",
        "Invalid Dates",
        "Invalid/Missing Salaries",
        "Invalid Employment Status",
        "Valid Records",
        "Invalid Records"
    ],

    "Count": [
        len(pd.read_excel(input_file)),
        len(df),
        missing_values.sum(),
        duplicate_rows,
        duplicate_employee_ids,
        len(invalid_employee_ids),
        len(invalid_dates),
        len(invalid_salary),
        len(invalid_status),
        len(valid),
        len(invalid)
    ]
})


# ============================================================
# 19. SAVE OUTPUT FILES
# ============================================================

df.to_excel(
    output_file,
    index=False
)

valid.to_excel(
    valid_file,
    index=False
)

invalid.to_excel(
    invalid_file,
    index=False
)

quality_report.to_excel(
    quality_file,
    index=False
)


# ============================================================
# 20. FINAL SUMMARY
# ============================================================

print("\n===================================")
print("DATA CLEANING COMPLETED")
print("===================================")

print("Rows after cleaning:", len(df))
print("Valid records:", len(valid))
print("Invalid records:", len(invalid))

print("\nFiles created:")
print("-", output_file)
print("-", valid_file)
print("-", invalid_file)
print("-", quality_file)