import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

#logging.info("Hello World")

list_of_files = [
   "src/__iniit__.py",
   "src/helper.py",
   "src/prompt.py",
   ".env",
   "requirement.txt",
   "setup.py",
   "research/trials.ipynb",
   "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    print(filedir, filename)

    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory (filedir) for the file (filename)")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating empty file (filepath)")
else:
    logging.info(f"(filename) is already exist")
    