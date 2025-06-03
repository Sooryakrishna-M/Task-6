# Task-6

🧾 Summary of the Process
I started with a raw dataset named Chocolate Sales.csv, which had uncleaned data — the dates were in text format and the revenue values in the Amount column included dollar signs and commas.

Using Python and Pandas in Jupyter Notebook, I:

Cleaned the Amount column by removing $ and , and converting it to float.

Converted the Date column into proper datetime format.

Added a synthetic order_id since it wasn’t available in the original dataset.

Then, I exported the cleaned dataset as Chocolate_Sales_Cleaned.csv.

After that, I moved to VS Code, where I wrote a Python script to:

Read the cleaned CSV.

Load it into a SQLite database (chocolate_sales.db) and create a table called chocolate_sales.

Using a SQLite extension in VS Code, I ran two SQL queries:

One to calculate monthly revenue and order volume by grouping and aggregating the data.

Another to find the top 3 revenue-generating months.

Finally, I organized everything (cleaned data, SQL script, database file, and README) and prepared it for GitHub submission.
