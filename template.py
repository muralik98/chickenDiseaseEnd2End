import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 

project_name = "cnnClassifier"

list_of_files = [

    ".github/workflows/.gitkeep", 
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
     "config/config.yaml",
     "dvc.yaml",
     "params.yaml",
     "requirement.txt",
     "setup.py",
     "research/trials.ipynb"

]

for filepath in list_of_files: 
    filepath = Path(filepath)             # Forward slash linux, windows backword. So Path will convert to windows path 
    fieldir, filename = os.path.split(filepath)

    if fieldir !="":
        os.makedirs(fieldir, exist_ok=True) 
        logging.info(f"Create Directory; {fieldir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):  # if not exisit or file size=0  
        with open(filepath, "w") as f:
            pass

            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists!")



