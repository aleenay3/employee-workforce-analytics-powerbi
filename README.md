# Employee Workforce Analytics | Power BI

## Project Overview

An interactive employee workforce analytics dashboard built using
Power BI, Excel, Power Query, DAX, and Python.

The project analyzes workforce composition, hiring, attrition,
salary, employee tenure, departments, locations, and workforce
movement.

## Business Questions

- How large is the current workforce?
- Which departments have the most employees?
- What is the average employee salary?
- How does workforce composition vary by department?
- What is the hiring and attrition trend?
- Which positions have higher average salaries?
- What is the employee tenure distribution?
- What factors are associated with salary differences?
- Are there data-quality issues?

## Tools & Technologies

Power BI • Power Query • DAX • Excel • Python • Pandas • OpenPyXL

## Dashboard Pages

### 1. Executive Overview

[insert screenshot]

Provides an executive-level overview of workforce size,
department distribution, gender composition, hiring trends,
and employment status.

### 2. Employee & Department Analysis

[insert screenshot]

Provides detailed analysis of salary, location, position,
department, gender, and employee-level information.

### 3. Workforce Trends & Insights

[insert screenshot]

Analyzes hiring, attrition, retention, workforce stability,
employee movement, and tenure.

### 4. Employee Profile

[insert screenshot]

Provides drill-through employee-level details.

## Power BI Features

- DAX measures
- Date table
- Active and inactive relationships
- Drill-through
- Bookmarks
- Collapsible filter panel
- What-If parameter
- Dynamic titles
- KPI variance
- Conditional formatting
- Key Influencers
- Decomposition Tree
- Interactive slicers

## Data Quality

Python automation performs:

- Required-column validation
- Missing-value detection
- Duplicate detection
- Duplicate Employee ID detection
- Date validation
- Salary validation
- Employment-status validation
- Valid/invalid record separation
- Automated Excel output

## Python Automation

The Python script uses Pandas to validate and transform the
employee dataset before it is used for analysis.

Generated outputs include:

- cleaned_employees.xlsx
- valid_employees.xlsx
- invalid_employees.xlsx
- data_quality_report.xlsx

## Key Skills Demonstrated

Data cleaning • Data validation • Data modeling • DAX •
Power Query • Business intelligence • KPI development •
Interactive reporting • Python automation • Excel automation