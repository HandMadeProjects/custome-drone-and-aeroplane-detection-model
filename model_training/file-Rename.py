import os

# folder_path = "aeroplane"  # Replace with the actual path to your folder
# folder_path = "drone_dataset"  # Replace with the actual path to your folder
folder_path = "noise"  # Replace with the actual path to your folder

# Ensure the folder path is valid
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Filter out only the files with the name "aeroplane"
    # aeroplane_files = [file for file in files if file.startswith("aeroplane")]

    # Rename the files with sequential numbers
    for i, old_name in enumerate(files):
        new_name = f"{i+1:06d}.jpg"  # Format the new name with leading zeros
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)

    print(f"Files of {folder_path} is renamed successfully !!!")
else:
    print("Invalid folder path.")
