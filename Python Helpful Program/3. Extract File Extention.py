import os

filename = "/path/to/your/file/example_file.mp3"
file_extension = os.path.splitext(filename)[1]
print(f"File extension method-1: {file_extension}")

#---------Method 2-----------
filename = "example_file.pdf"
file_extension = filename.split(".")[-1]
print(f"File extension method-2: {file_extension}")

#--------Method 3---------------
from pathlib import Path

filename = "example_file.mp4"
file_extension = Path(filename).suffix
print(f"File extension method-3: {file_extension}")
