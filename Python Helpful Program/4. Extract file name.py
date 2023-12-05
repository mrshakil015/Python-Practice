import os

file_path = "/path/to/your/file/example_file.mp3"
file_name = os.path.basename(file_path)
print(f"File name method-1: {file_name}")

#------- Method 2-----------
from pathlib import Path

file_path = "/path/to/your/file/example_file.mp3"
file_name = Path(file_path).name
print(f"File name method-2: {file_name}")

