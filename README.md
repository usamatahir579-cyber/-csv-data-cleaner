# CSV Data Cleaner Tool

##  Project Overview
This is a simple Python project that cleans messy CSV business data.  
It reads raw CSV files, processes the data, and generates a cleaned version by fixing common data issues.

---

## Features
- Reads CSV files using Python file handling
- Handles missing values in data
- Fixes invalid age entries (non-numeric values)
- Removes duplicate rows
- Saves cleaned data into a new CSV file

# CSV Data Cleaner Tool

## Project Overview
This is a simple Python project that cleans messy CSV business data.  
It reads raw CSV files, processes the data, and generates a cleaned version by fixing common data issues.

---

## Features
- Reads CSV files using Python file handling
- Handles missing values in data
- Fixes invalid age entries (non-numeric values)
- Removes duplicate rows
- Saves cleaned data into a new CSV file

---

## Input Format Example
name,age,salary  
Ali,25,50000  
Sara,,60000  
John,thirty,70000  
Ali,25,50000  

---

## Output Example
Ali,25,50000  
Sara,0,60000  
John,0,70000  

- Missing or invalid ages are replaced with `0`
- Duplicate rows are removed

---

##  How to Run
1. Place your CSV file as `data.csv`
2. Run the script:

python main.py

3. Output will be saved as:
cleaned_data.csv

---

## Project Logic
- Read CSV file line by line  
- Split data into columns  
- Validate and clean data  
- Remove duplicates  
- Save cleaned dataset  

---

## Author
Usama Tahir
