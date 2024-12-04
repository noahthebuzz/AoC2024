import os
import requests

# Create the folders needed for the 'Advent Of Code' event
def setup_aoc_structure():

        # Define the number of days for Advent of Code
        num_days = 24

        parent_folder = "W:\git\GitHub\Privat\AoC2024"
        
        # Create directories and files for each day
        for day in range(1, num_days + 1):

                # Format the folder name (e.g., day01, day02, ...)
                folder_name = f"day{day:02}"

                # Create the folder if it doesn't already exist
                os.makedirs(folder_name, exist_ok=True)

                # Define the file names
                files_to_create = ["input.txt", "task.txt", "solution.py"]

                for file_name in files_to_create:
                       # Create the file path
                        file_path = os.path.join(folder_name, file_name)

                         # Create the file if it doesn't already exist
                        if not os.path.exists(file_path):
                                with open(file_path, "w") as f:
                                        if file_name == "solution.py":
                                                # Add a comment to the Python solution file as a placeholder
                                                f.write("# Write your solution here\n")
                                                # Add this:
                                                ## Read input from file
                                                #path = "W:\git\GitHub\Privat\AoC2024\day04\input.txt"
                                                #with open(path, 'r') as file:
                                                        #data = file.readlines()
                                                f.write("\n\n# Read input from file\n")
                                                f.write(f"path = \"{parent_folder}\\{folder_name}\\input.txt\"\n")
                                                f.write("with open(path, 'r') as file:\n")
                                                f.write("        data = file.readlines()\n")

                                        else:
                                                # Leave the other files empty
                                                pass

        print(f"Advent of Code structure set up with folders and files for {num_days} days!")

def download_input():
        # Get the year and day number from the user
        year = input("Enter the year (e.g., 2024): ").strip()
        day_number = input("Enter the day number (1-24): ").strip()

        # Format the URL for downloading input
        url = f"https://adventofcode.com/{year}/day/{day_number}/input"

        # Get the folder name based on the day number
        folder_name = f"day{int(day_number):02}"
        input_file_path = os.path.join(folder_name, "input.txt")

        

# Run the program
if __name__ == "__main__":
        setup_aoc_structure()
        #download_input()