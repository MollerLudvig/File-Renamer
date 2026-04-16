import os

from tkinter import Tk
from tkinter.filedialog import askdirectory

import re

path = askdirectory(title='Select Folder') # shows dialog box and return the path


for filename in os.listdir(path):
    base_name, ext = os.path.splitext(filename)
    match = re.match(r"^(.*)\(\s*(\d+x\d+[^)]*)\s*\)$", base_name)
    
    name, dims = match.groups()
    name = name.strip()

    new_name = f"{dims} - {name}{ext}"

    old_file = os.path.join(path, filename)
    new_file = os.path.join(path, new_name)

    os.rename(old_file, new_file)

    print(f"{filename} → {new_name}")   

