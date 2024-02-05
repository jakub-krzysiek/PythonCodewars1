import os

def replace_underscores(folder_path):
    for filename in os.listdir(folder_path):
        if '_' in filename:
            new_filename = filename.replace('_', ' ')
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)

# Replace 'your_folder_path' with the actual path to your folder
folder_path = r'C:\Git\PythonCodewars1\RockPaperScissors (6kyu)'
replace_underscores(folder_path)