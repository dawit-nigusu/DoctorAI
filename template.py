import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    '.env',
    'requirements.txt',
    'setup.py',
    'app.py',
    'research/trails.ipynb',
]

for filepath in list_of_files:
    # Create the directory if it doesn't exist
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory: {directory}")

    # Create the file if it doesn't exist
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            f.write("# This is a placeholder file.\n")
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")