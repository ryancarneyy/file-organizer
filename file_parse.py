import os
import time




def clean_dir(directory, time):
    # Get the current time in seconds
    current_time = time.time()

    # Calculate the time for one year ago (in seconds)
    one_year_ago = current_time - (365 * 24 * 3600)

    # Initialize a list to store file paths
    old_files = []

    # Iterate through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)
            
            try:
                # Get the last access time of the file
                last_access_time = os.path.getatime(file_path)
                
                # Check if the file hasn't been accessed in one year
                if last_access_time < one_year_ago and not "/Users/ryancarney/Documents/FileOrganizer" in file_path:
                    old_files.append(file_path)
            except FileNotFoundError:
                print(f"File not found: {file_path}")

    # Print the list of old file paths
    return old_files


