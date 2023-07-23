import os
import shutil

# Define the source directory where the files are located
source_dir = 'C:\Downloads\Video'

# Get a list of all files in the source directory
files = os.listdir(source_dir)

# Iterate over the files
for filename in files:
    if filename.endswith('.mp4'): # Whatever it needs to be for you.
        # Extract the name part of the filename
        name = filename.split(' Episode ')[0]

        # Create the destination folder if it doesn't exist
        destination_folder = os.path.join(source_dir, name)
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file to the destination folder
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_folder, filename)
        shutil.move(source_file, destination_file)

        print(f"Moved {filename} to {destination_folder}")
