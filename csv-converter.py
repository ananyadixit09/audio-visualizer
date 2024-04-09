import os
import csv

# Set the root directory where your audio folders are located
root_dir = "/Users/aaryansinghrajput/Developer/audio-visualizer/data"

# Create an empty list to store the data
data = []

# Loop through the directories in the root directory
for dir_name in os.listdir(root_dir):
    dir_path = os.path.join(root_dir, dir_name)

    # Check if the current item is a directory
    if os.path.isdir(dir_path):
        # Loop through the files in the directory
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)

            # Check if the current item is a file
            if os.path.isfile(file_path):
                # Add the file path and class label to the data list
                data.append([file_path, dir_name])

# Create a CSV file and write the data
with open("audio_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["file_path", "class"])  # Write the header row
    writer.writerows(data)  # Write the data rows

print("CSV file created successfully.")