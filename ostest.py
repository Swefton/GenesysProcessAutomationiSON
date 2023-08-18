import os

def rename_newest_file(directory):
    # List all files in the directory along with their timestamps
    files = [(file, os.path.getmtime(os.path.join(directory, file))) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        
    if not files:
        return None
    
    # Find the file with the latest timestamp
    newest_file = max(files, key=lambda item: item[1])[0]
    os.rename(directory + '\\' + newest_file,directory + '\\' + '(1) ' + newest_file)


# Specify the directory path
directory_path = r'C:\Users\thelo\OneDrive\Desktop\Internship\Scraper\downloads'

newest_file = rename_newest_file(directory_path)


