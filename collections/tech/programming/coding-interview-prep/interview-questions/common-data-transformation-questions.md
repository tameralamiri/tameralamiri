Question 1: Data Cleaning and Preparation
Task:
You have a DataFrame named df containing user data with the following columns: UserID, Name, Age, and Email. Some of the Email entries are missing, and the Age column includes negative values which are errors. Write a Python script using Pandas to:

Remove any rows where Email is missing.
Replace negative values in the Age column with the average age of the DataFrame, excluding negative values.



Question 2: Data Grouping and Aggregation
Task:
Consider a DataFrame df that includes sales data with columns Date, ProductID, Price, and Quantity. Write a Python script to calculate the total revenue (Price * Quantity) per product for each month. The Date column is in the format 'YYYY-MM-DD'.


Question 3: Merging DataFrames
Task:
You are given two DataFrames, df1 and df2. DataFrame df1 contains columns UserID and Name, and DataFrame df2 contains columns UserID and PurchaseAmount. Merge these two DataFrames to create a new DataFrame that includes the user's name next to their purchase amount. Ensure all users from df1 are included in the result, even if they don't have any purchases listed in df2.

Question 4: Data Filtering
Task:
Write a Python script to filter rows in a DataFrame df containing columns Product, Category, and Price. You need to find all products in the "Electronics" category that have a price greater than 500. The result should be a new DataFrame with the same columns.

Question 5: Pivoting and Reshaping Data
Task:
Given a DataFrame df with columns Year, Month, Product, and Sales, write a Python script to create a pivot table that shows the total sales for each product per month. The Year and Month should be combined into a single date column in the format 'YYYY-MM'.

Question 6: Working with Date and Time
Task:
You have a DataFrame df with a column Timestamp containing POSIX timestamp values. Convert these timestamps into a human-readable date format and create a new column Date that includes the result.

Question 7: Advanced Data Transformation
Task:
A DataFrame df contains a column Data with JSON strings like {'a': 1, 'b': 2}. Write a Python script using Pandas to parse these JSON strings and create two new columns in the DataFrame, a and b, containing the corresponding values from the JSON.

