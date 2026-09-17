[README (10).md](https://github.com/user-attachments/files/32335899/README.10.md)
# Sales Data Analyzer

A command-line Python tool for loading, exploring, cleaning, analyzing, and visualizing sales data from CSV files. Built around a simple menu-driven interface, it wraps common `pandas`, `numpy`, and `matplotlib` workflows into an interactive experience — no coding required to explore a dataset.

## Features

- **Load Dataset** — Load any CSV file into a pandas DataFrame (auto-strips whitespace from column headers to avoid `KeyError` issues).
- **Explore Data** — View the first/last 5 rows, column names, data types, and general dataset info.
- **DataFrame Operations** — Filter rows, sort by column, build pivot tables, run group-by aggregations, and convert columns to NumPy arrays.
- **Handle Missing Data** — Detect missing values, fill numeric columns with the mean, drop incomplete rows, or replace missing values with a custom value.
- **Generate Descriptive Statistics** — Quick `describe()` summary across all columns.
- **Data Visualization** — Create bar plots, line plots, scatter plots, pie charts, histograms, and stack plots.
- **Save Visualization** — Export the most recently generated plot to an image file (e.g., PNG).

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

Install dependencies with:

```bash
pip install pandas numpy matplotlib seaborn
```

## Usage

Run the script from the terminal:

```bash
python PR_9_VISUALIZER.py
```

You'll be greeted with the main menu:

```
========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================
```

Enter a number to select an option, and follow the on-screen prompts.

## Example Walkthrough

The following is a sample session demonstrating the core workflow: loading data, exploring it, checking for missing values, generating a plot, and saving it.

### 1. Load a Dataset

```
Enter your choice:  1

== Load Dataset ==
Enter the path of the dataset (CSV file):  data/sales_data.csv
Dataset loaded successfully!
```

### 2. Explore the Data

Selecting **Explore Data → Display the first 5 rows** shows a preview of the dataset:

```
   SalesID   Product    Region      Sales  Profit  Year
0      101  Product A   North        500    100    2022
1      102  Product B   East         600    150    2022
2      103  Product C   West Coast   700    180    2022
3      104  Product D   South        800    220    2022
4      105  Product E   Central      550    110    2022
```

### 3. Handle Missing Data

Checking for missing values confirms the dataset is clean:

```
== Handle Missing Data ==
1. Display rows with missing values
...
Enter your choice:  1

No missing values found in the dataset!
```

### 4. Generate a Visualization

Choosing **Data Visualization → Scatter Plot** and specifying `SalesID` and `Year` as the axes produces a scatter plot:

```
== Data Visualization ==
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
7. Back to Main Menu
Enter your choice:  3
Enter x-axis column name: SalesID
Enter y-axis column name: Year
Generating plot...
```

This renders a chart titled **"Scatter Plot: SalesID vs Year"**, plotting each `SalesID` against its corresponding `Year`.

### 5. Save the Visualization

```
== Save Visualization ==
Enter file name to save the plot (e.g., scatter_plot.png):  scatter_plot.png
Visualization saved as scatter_plot.png successfully!
```

### 6. Exit

```
Enter your choice:  8

Exiting the program. Goodbye!
```

## Project Structure

```
.
├── PR_9_VISUALIZER.py     # Main application script
├── data/
│   └── sales_data.csv     # Example dataset (user-provided)
└── README.md              # Project documentation
```

## Notes

- Column headers are automatically stripped of leading/trailing whitespace on load to prevent `KeyError` issues when referencing column names.
- All visualization options include validation to catch invalid or mistyped column names and will list the available columns if an error occurs.
- The most recently generated plot is held in memory and can be saved at any time via the **Save Visualization** menu option.

## License

This project is provided as-is for educational and personal use.

## Author

Pankti Patel
