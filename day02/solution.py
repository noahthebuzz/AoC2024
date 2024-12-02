

# Function to check if a report is safe
def is_safe(report):
    differences = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
    # Check if differences are all between 1 and 3
    if not all(1 <= diff <= 3 for diff in differences):
        return False

    # Check if the report is strictly increasing or decreasing
    if all(report[i] < report[i + 1] for i in range(len(report) - 1)) or \
       all(report[i] > report[i + 1] for i in range(len(report) - 1)):
        return True

    return False

# Function to check if a report can be made safe by removing one level
def can_be_safe_with_removal(report):
    for i in range(len(report)):
        # Create a new report with one level removed
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

# Read input from file
path = "W:\git\GitHub\Privat\AoC2024\day02\input.txt"
with open(path, 'r') as file:
    data = file.readlines()

# Parse the input into reports
reports = [list(map(int, line.split())) for line in data]


# Count the number of safe reports
safe_reports_count = sum(1 for report in reports if is_safe(report))

print("Number of safe reports (without Problem Dampener):", safe_reports_count)


# Count the number of safe reports with dampener
safe_reports_count = sum(1 for report in reports if is_safe(report) or can_be_safe_with_removal(report))

print("Number of safe reports (with Problem Dampener):", safe_reports_count)
