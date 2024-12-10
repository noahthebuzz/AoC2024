import os
import requests

# Create the folders needed for the 'Advent Of Code' event
def setup_aoc_structure():

        # Define the number of days for Advent of Code
        num_days = 25
        
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
                                                f.write("import sys\n")
                                                f.write("import re\n")
                                                f.write("from collections import defaultdict, Counter, deque\n")
                                                f.write("import pyperclip as pc\n")
                                                # Add this:
                                                ## Read input from file
                                                #path = "W:\git\GitHub\Privat\AoC2024\day04\input.txt"
                                                #with open(path, 'r') as file:
                                                        #data = file.readlines()
                                                f.write("\n\n# Read input from file\n")
                                                f.write(f"path = \"{folder_name}\\input.txt\"\n")
                                                f.write("data = open(path).read().strip()")
                                                f.write("print(data)\n")

                                        else:
                                                # Leave the other files empty
                                                pass

        print(f"Advent of Code structure set up with folders and files for {num_days} days!")


# Run the program
if __name__ == "__main__":
        setup_aoc_structure()
        #download_input()