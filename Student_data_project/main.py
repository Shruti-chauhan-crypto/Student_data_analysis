from src.load_data import load_data
from src.load_data import inspect_data
from src.clean_data import clean_data
from src.transform import transform_data
from src.filter_data import filter_data
from src.analyze import analyze_data
from src.analyze import sort_data
from src.analyze import group_data
from src.report import generate_report

print("========== Student Data Analysis Project ==========\n")

# Step 1: Load Dataset
df = load_data()
print("Dataset loaded successfully.\n")

# Step 2: Inspect Dataset
print("Inspecting Dataset...")
inspect_data(df)
print()

# Step 3: Clean Dataset
print("Cleaning Dataset...")
df = clean_data(df)
print("Cleaning completed.\n")

# Step 4: Transform Dataset
print("Transforming Dataset...")
df = transform_data(df)
print("Transformation completed.\n")

# Step 5: Filter Dataset
print("Filtering Dataset...")
filter_data(df)
print("Filtering completed.\n")

# Step 6: Analyze Dataset
print("Analyzing Dataset...")
analyze_data(df)

# Step 7: Sort Dataset
print("Sorting Dataset...")
sort_data(df)

# Step 8: Group Data
print("Grouping Dataset...")
group_data(df)

# Step 9: Generate Report
generate_report(df)
print("Report generated")

print("========== Project Executed Successfully ==========")
