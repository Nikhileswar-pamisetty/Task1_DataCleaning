# Task1_DataCleaning
Loads a CSV dataset into a pandas DataFrame.
Removes duplicate rows.
Standardizes column names to lowercase with underscores, and renames 'no-show' column to 'no_show'.
Cleans and standardizes text data in 'gender' and 'no_show' columns (uppercase, stripped spaces).
Converts date columns to datetime format.
Formats 'patientid' as string with one decimal place to avoid scientific notation, but IDs are typically numeric and can be converted back to integers for accurate numeric handling.
Cleans 'age' by converting to integers and removing invalid ages (<0).
Sets appropriate data types for categorical and numeric columns, including converting IDs back to integers if needed.
Saves the cleaned DataFrame back to a CSV file.
