import os
import random
import string

def generate_random_name(length=8):
    """Generate a random folder name of a specified length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_content(length=20):
    """Generate random content for text files."""
    return ''.join(random.choice(string.ascii_letters + ' ') for _ in range(length))

def create_folders_with_content(base_path, num_folders=10, num_files_per_folder=3):
    """Create specified number of folders with random names and random content."""
    for i in range(num_folders):
        if i == 0:  # First folder will be "Ice Berg Tongue"
            folder_name = "Ice Berg Tongue"
        else:
            folder_name = generate_random_name()
        
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        # Create random text files in the folder
        for j in range(num_files_per_folder):
            file_name = f"file_{j + 1}.txt"
            file_path = os.path.join(folder_path, file_name)
            content = generate_random_content()
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"Created file: {file_path}")

if __name__ == "__main__":
    base_directory = "your_directory_here"  # Change this to your desired directory
    create_folders_with_content(base_directory)

