# Employee Workforce Analytics — Data Dictionary

## Project Overview

This data dictionary describes the fields used in the Employee Workforce Analytics project.

The dataset is used for workforce analysis in Power BI and data-quality validation and automation using Python.

> **Data Note:** This portfolio project uses sample data. No confidential or real employee information should be included.

---

## Employee Data Fields

| Field | Data Type | Description |
|---|---|---|
| `EmployeeID` | Integer | Unique identifier for each employee. |
| `EmployeeCode` | Text | Employee reference code. |
| `EmployeeName` | Text | Employee name used for employee-level analysis. |
| `Gender` | Text | Employee gender category. |
| `DateOfBirth` | Date | Employee date of birth, used for age analysis. |
| `Department` | Text | Department in which the employee works. |
| `Position` | Text | Employee job position or role. |
| `Location` | Text | Employee work location or city. |
| `JoiningDate` | Date | Date the employee joined the organization. |
| `LeavingDate` | Date | Date the employee left the organization. Blank when no leaving date is recorded. |
| `MonthlySalaryPKR` | Decimal | Employee monthly salary in Pakistani Rupees (PKR). |
| `EmploymentStatus` | Text | Employee employment status, such as Active, Resigned, or On Leave. |

---

## Derived Power BI Fields

| Field | Type | Description |
|---|---|---|
| `Year` | Integer | Year derived from the DateTable. |
| `Month Name` | Text | Month name used for monthly trend analysis. |
| `Month Number` | Integer | Numeric month used to sort Month Name chronologically. |
| `Tenure Band` | Text | Employee tenure category calculated from JoiningDate and LeavingDate/current date. |

### Tenure Bands

- `< 1 Year`
- `1–3 Years`
- `3–5 Years`
- `5–10 Years`
- `10+ Years`

---

## Key Power BI Measures

| Measure | Description |
|---|---|
| `Total Employees` | Distinct count of employees based on EmployeeID. |
| `Active Employees` | Count of employees whose status is Active. |
| `Department Count` | Number of distinct departments. |
| `Average Salary` | Average monthly employee salary. |
| `Average Age` | Average employee age calculated from DateOfBirth. |
| `New Hires` | Employee count used for hiring analysis. |
| `Attrition Count` | Employees with an attrition status and leaving date. |
| `Attrition Rate` | Attrition count divided by total employees. |
| `Average Tenure (Years)` | Average employee tenure in years. |
| `Employees On Leave` | Count of employees with On Leave status. |
| `Current Workforce` | Count of currently active employees. |
| `Hiring Rate` | New hires divided by total employees. |
| `Retention Rate` | Employees retained relative to total employees. |
| `Workforce Stability` | Current workforce divided by total employees. |

---

## Data Quality Validation

Python automation validates the employee dataset for:

- Required columns
- Missing values
- Duplicate rows
- Duplicate Employee IDs
- Invalid Employee IDs
- Invalid dates
- Missing or invalid salaries
- Invalid employment statuses
- Valid and invalid record separation

---

## Data Cleaning

The Python automation performs several transformations:

- Removes leading and trailing whitespace
- Standardizes text values
- Standardizes gender values
- Standardizes department names
- Standardizes locations
- Converts date fields to valid date formats
- Converts salary values to numeric values
- Removes duplicate rows
- Calculates employee tenure

---

## Business Rules

### Employee ID

`EmployeeID` is expected to uniquely identify an employee.

### Leaving Date

A blank `LeavingDate` indicates that no leaving date is recorded.

For active employees, the current date is used when calculating tenure.

### Salary

Missing salary values are not automatically replaced with zero.

Missing values should be investigated or handled using an appropriate and documented business rule.

### Date Validation

A record is considered invalid when:

`LeavingDate < JoiningDate`

### Employment Status

Valid employment statuses include:

- Active
- Resigned
- On Leave
- Terminated

---

## Data Flow

```text
Excel Dataset
      ↓
Python / Pandas
      ↓
Data Quality Validation
      ↓
Data Cleaning & Transformation
      ↓
Cleaned Dataset
      ↓
Power BI
      ↓
Power Query
      ↓
Data Model + DAX
      ↓
Interactive Workforce Analytics Dashboard