from src.load_data import load_data
from src.load_data import inspect_data
from src.clean_data import clean_data
from src.transform import transform_data
from src.filter_data import filter_data
from src.analyze import analyze_data
from src.analyze import sort_data
from src.analyze import group_data
from src.report import generate_report

def menu():
    print("\n========== Student Data Analysis ==========")
    print("1. Load Dataset")
    print("2. Inspect Dataset")
    print("3. Clean Dataset")
    print("4. Transform Dataset")
    print("5. Filter Dataset")
    print("6. Analyze Dataset")
    print("7. Sort Dataset")
    print("8. Group Data")
    print("9. Generate Report")
    print("10. Run Complete Project")
    print("0. Exit")

while True:
    menu()
    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            df = load_data()
            print("Dataset Loaded Successfully!")

        case 2:
            if df is None:
                print("Please load the dataset first.")
            else:
                inspect_data(df)

        case 3:
            if df is None:
                print("Please load the dataset first.")
            else:
                df = clean_data(df)
                print("Dataset Cleaned Successfully!")

        case 4:
            if df is None:
                print("Please load the dataset first.")
            else:
                df = transform_data(df)
                print("Transformation Completed!")

        case 5:
            if df is None:
                print("Please load the dataset first.")
            else:
                filter_data(df)
                print("Filtered Files Created!")

        case 6:
            if df is None:
                print("Please load the dataset first.")
            else:
                analyze_data(df)

        case 7:
            if df is None:
                print("Please load the dataset first.")
            else:
                sort_data(df)

        case 8:
            if df is None:
                print("Please load the dataset first.")
            else:
                group_data(df)

        case 9:
            if df is None:
                print("Please load the dataset first.")
            else:
                generate_report(df)
                print("Report generated")

        case 10:
            df = load_data()
            inspect_data(df)
            df = clean_data(df)
            df = transform_data(df)
            filter_data(df)
            analyze_data(df)
            sort_data(df)
            group_data(df)
            generate_report(df)

            print("\nProject Executed Successfully!")

        case 0:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice! Please try again.")


# print("========== Student Data Analysis Project ==========\n")

# # Step 1: Load Dataset
# df = load_data()
# print("Dataset loaded successfully.\n")

# # Step 2: Inspect Dataset
# print("Inspecting Dataset...")
# inspect_data(df)
# print()

# # Step 3: Clean Dataset
# print("Cleaning Dataset...")
# df = clean_data(df)
# print("Cleaning completed.\n")

# # Step 4: Transform Dataset
# print("Transforming Dataset...")
# df = transform_data(df)
# print("Transformation completed.\n")

# # Step 5: Filter Dataset
# print("Filtering Dataset...")
# filter_data(df)
# print("Filtering completed.\n")

# # Step 6: Analyze Dataset
# print("Analyzing Dataset...")
# analyze_data(df)

# # Step 7: Sort Dataset
# print("Sorting Dataset...")
# sort_data(df)

# # Step 8: Group Data
# print("Grouping Dataset...")
# group_data(df)

# # Step 9: Generate Report
# generate_report(df)
# print("Report generated")

# print("========== Project Executed Successfully ==========")
