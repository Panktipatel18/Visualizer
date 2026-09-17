import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:
    def _init_(self, file_path=None):
        """Constructor: Initializes the class and optionally loads a dataset."""
        self.data = None
        self.last_fig = None
        if file_path:
            self.load_data(file_path)

    def _del_(self):
        """Destructor: Cleanup method when object is destroyed."""
        pass

    def load_data(self, file_path):
        """Load data from a CSV file into a pandas DataFrame."""
        try:
            self.data = pd.read_csv(file_path)
            # Remove hidden leading/trailing spaces in column headers (Fixes KeyError)
            self.data.columns = self.data.columns.str.strip()
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading dataset: {e}")

    # =========================================================================
    # 2. EXPLORE DATA
    # =========================================================================
    def explore_data(self):
        if self.data is None:
            print("No dataset loaded! Please load a dataset first.")
            return

        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                print("\n", self.data.head())
            elif choice == "2":
                print("\n", self.data.tail())
            elif choice == "3":
                print("\nColumn Names:")
                for col in self.data.columns:
                    print(f"- {col}")
            elif choice == "4":
                print("\nData Types:\n", self.data.dtypes)
            elif choice == "5":
                print("\nBasic Info:")
                self.data.info()
            elif choice == "6":
                break
            else:
                print("Invalid choice! Please try again.")

    # =========================================================================
    # 3. DATAFRAME OPERATIONS & ADVANCED OPERATIONS
    # =========================================================================
    def dataframe_operations(self):
        if self.data is None:
            print("No dataset loaded! Please load a dataset first.")
            return

        while True:
            print("\n== Perform DataFrame Operations ==")
            print("1. Filter Data")
            print("2. Sort Data")
            print("3. Create Pivot Table")
            print("4. Perform GroupBy Aggregation")
            print("5. Convert Column to NumPy Array & Slice")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                col = input("Enter column to filter by: ").strip()
                if col in self.data.columns:
                    val = input(f"Enter value for {col}: ").strip()
                    filtered = self.data[self.data[col].astype(str) == val]
                    print("\nFiltered Result:\n", filtered)
                else:
                    print(f"Column '{col}' not found.")

            elif choice == "2":
                col = input("Enter column to sort by: ").strip()
                if col in self.data.columns:
                    asc_input = input("Ascending? (y/n): ").strip().lower()
                    asc = asc_input == "y"
                    sorted_df = self.data.sort_values(by=col, ascending=asc)
                    print("\nSorted Data:\n", sorted_df.head())
                else:
                    print(f"Column '{col}' not found.")

            elif choice == "3":
                index_col = input("Enter index column: ").strip()
                val_col = input("Enter values column: ").strip()
                agg_func = input("Enter aggfunc (mean, sum, count): ").strip()
                if index_col in self.data.columns and val_col in self.data.columns:
                    pivot = pd.pivot_table(
                        self.data,
                        values=val_col,
                        index=index_col,
                        aggfunc=agg_func,
                    )
                    print("\nPivot Table:\n", pivot)
                else:
                    print("Invalid columns specified.")

            elif choice == "4":
                group_col = input("Enter group-by column: ").strip()
                num_col = input("Enter target numerical column: ").strip()
                if group_col in self.data.columns and num_col in self.data.columns:
                    res = self.data.groupby(group_col)[num_col].agg(
                        ["sum", "mean", "count"]
                    )
                    print("\nGroupBy Results:\n", res)
                else:
                    print("Invalid columns specified.")

            elif choice == "5":
                col = input("Enter column to convert to NumPy array: ").strip()
                if col in self.data.columns:
                    arr = self.data[col].to_numpy()
                    print(f"\nNumPy Array Shape: {arr.shape}")
                    print(f"First 5 elements: {arr[:5]}")
                else:
                    print(f"Column '{col}' not found.")

            elif choice == "6":
                break
            else:
                print("Invalid choice! Please try again.")

    # =========================================================================
    # 4. HANDLE MISSING DATA
    # =========================================================================
    def handle_missing_data(self):
        if self.data is None:
            print("No dataset loaded! Please load a dataset first.")
            return

        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                null_rows = self.data[self.data.isnull().any(axis=1)]
                if null_rows.empty:
                    print("\nNo missing values found in the dataset!")
                else:
                    print("\nRows with missing values:\n", null_rows)

            elif choice == "2":
                numeric_cols = self.data.select_dtypes(
                    include=[np.number]
                ).columns
                self.data[numeric_cols] = self.data[numeric_cols].fillna(
                    self.data[numeric_cols].mean()
                )
                print("\nMissing numeric values filled with column means.")

            elif choice == "3":
                self.data.dropna(inplace=True)
                print("\nRows with missing values dropped.")

            elif choice == "4":
                val = input("Enter value to replace NaNs with: ").strip()
                self.data.fillna(val, inplace=True)
                print(f"\nMissing values replaced with '{val}'.")

            elif choice == "5":
                break
            else:
                print("Invalid choice! Please try again.")

    # =========================================================================
    # 5. GENERATE DESCRIPTIVE STATISTICS
    # =========================================================================
    def generate_statistics(self):
        if self.data is None:
            print("No dataset loaded! Please load a dataset first.")
            return

        print("\n== Descriptive Statistics ==")
        print(self.data.describe(include="all"))

    # =========================================================================
    # 6. DATA VISUALIZATION
    # =========================================================================
    def data_visualization(self):
        if self.data is None:
            print("No dataset loaded! Please load a dataset first.")
            return

        while True:
            print("\n== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Back to Main Menu")

            choice = input("Enter your choice: ").strip()

            if choice in ["1", "2", "3"]:
                x_col = input("Enter x-axis column name: ").strip()
                y_col = input("Enter y-axis column name: ").strip()

                # Safety check to prevent KeyError
                if x_col not in self.data.columns or y_col not in self.data.columns:
                    print(
                        f"\nError: Available columns are {list(self.data.columns)}"
                    )
                    continue

                fig, ax = plt.subplots(figsize=(8, 5))
                if choice == "1":
                    ax.bar(self.data[x_col], self.data[y_col])
                    ax.set_title(f"Bar Plot: {x_col} vs {y_col}")
                elif choice == "2":
                    ax.plot(self.data[x_col], self.data[y_col], marker="o")
                    ax.set_title(f"Line Plot: {x_col} vs {y_col}")
                elif choice == "3":
                    ax.scatter(self.data[x_col], self.data[y_col])
                    ax.set_title(f"Scatter Plot: {x_col} vs {y_col}")

                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                plt.xticks(rotation=45)
                plt.tight_layout()
                self.last_fig = fig
                print(f"Generating plot...")
                plt.show()

            elif choice == "4":
                col = input("Enter categorical column name for Pie Chart: ").strip()
                if col in self.data.columns:
                    fig, ax = plt.subplots(figsize=(6, 6))
                    counts = self.data[col].value_counts()
                    ax.pie(counts, labels=counts.index, autopct="%1.1f%%")
                    ax.set_title(f"Pie Chart of {col}")
                    self.last_fig = fig
                    plt.show()
                else:
                    print(f"Column '{col}' not found.")

            elif choice == "5":
                col = input("Enter numerical column name for Histogram: ").strip()
                if col in self.data.columns:
                    fig, ax = plt.subplots(figsize=(8, 5))
                    ax.hist(self.data[col], bins=10, edgecolor="black")
                    ax.set_title(f"Histogram of {col}")
                    ax.set_xlabel(col)
                    ax.set_ylabel("Frequency")
                    self.last_fig = fig
                    plt.show()
                else:
                    print(f"Column '{col}' not found.")

            elif choice == "6":
                x_col = input("Enter x-axis column: ").strip()
                y1_col = input("Enter first numerical y-column: ").strip()
                y2_col = input("Enter second numerical y-column: ").strip()
                if (
                    x_col in self.data.columns
                    and y1_col in self.data.columns
                    and y2_col in self.data.columns
                ):
                    fig, ax = plt.subplots(figsize=(8, 5))
                    ax.stackplot(
                        self.data[x_col],
                        self.data[y1_col],
                        self.data[y2_col],
                        labels=[y1_col, y2_col],
                    )
                    ax.legend(loc="upper left")
                    ax.set_title(f"Stack Plot of {y1_col} and {y2_col} over {x_col}")
                    self.last_fig = fig
                    plt.show()
                else:
                    print("One or more column names are invalid.")

            elif choice == "7":
                break
            else:
                print("Invalid choice! Please try again.")

    # =========================================================================
    # 7. SAVE VISUALIZATION
    # =========================================================================
    def save_visualization(self):
        if self.last_fig is None:
            print("\nNo visualization available to save! Generate a plot first.")
            return

        print("\n== Save Visualization ==")
        filename = input(
            "Enter file name to save the plot (e.g., scatter_plot.png): "
        ).strip()
        if filename:
            try:
                self.last_fig.savefig(filename, bbox_inches="tight")
                print(f"Visualization saved as {filename} successfully!")
            except Exception as e:
                print(f"Error saving image: {e}")
        else:
            print("Filename cannot be empty.")


# ==============================================================================
# MAIN PROGRAM FLOW
# ==============================================================================
def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("===========================================================")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\n== Load Dataset ==")
            path = input(
                "Enter the path of the dataset (CSV file): "
            ).strip()
            analyzer.load_data(path)
        elif choice == "2":
            analyzer.explore_data()
        elif choice == "3":
            analyzer.dataframe_operations()
        elif choice == "4":
            analyzer.handle_missing_data()
        elif choice == "5":
            analyzer.generate_statistics()
        elif choice == "6":
            analyzer.data_visualization()
        elif choice == "7":
            analyzer.save_visualization()
        elif choice == "8":
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid selection!")
            print("Please enter a number between 1 and 8.")


if __name__ == "_main_":
    main()