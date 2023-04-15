import os
from glob import glob
from pathlib import Path
import re
from pdfminer.high_level import extract_text
import unicodedata

def rename_files(path):
    file = glob(path)
    f = open("error.txt", "w")
    for path in file:
        text = extract_text(path).split("\n")
        try:
            new_pdf_name = unicodedata.normalize("NFKD", re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '-', text[2]).strip(" ")) + ".pdf"
            print(new_pdf_name)
            parent_path = Path(path).parent
            os.rename(path, dst=os.path.join(parent_path, new_pdf_name))
        except:
            f.write(path + "\n") 
    f.close()