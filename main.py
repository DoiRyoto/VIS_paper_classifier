from pdf_name import rename_files
from crawler import get_sessions_article_dict, get_session_list
import os
import re
from pathlib import Path
import shutil
from glob import glob
import unicodedata
from pathlib import Path
import numpy as np


link = "https://ieeevis.org/year/2022/info/papers-sessions"
sessions_article_dict = get_sessions_article_dict(link)
session_list = get_session_list(link)

sum = 0
idx_list = []
for article_list in sessions_article_dict.values():
    sum += len(article_list)
    idx_list.append(len(article_list))

""" 
rename_path = "pdfs/*/*/*.pdf"
# rename_files(rename_path)

for i, session_name in enumerate(session_list):
    session_name = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '-', session_name)
    os.makedirs(os.path.join("outputs", "{}_".format(str(i + 1).zfill(2)) + session_name), exist_ok=True)

file = glob("pdfs/*/*/*.pdf")

for path in file:
    basename = os.path.basename(path)
    basename = basename[:basename.find(".pdf")]
    for i, session_name in enumerate(session_list):
        article_name_list = sessions_article_dict[session_name]

        session_name = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '-', session_name)
        dst_path = os.path.join("outputs", "{}_".format(str(i + 1).zfill(2)) + session_name)
        for article_name in article_name_list:
            if unicodedata.normalize("NFKD", basename.lower().replace(" ", "")) in unicodedata.normalize("NFKD", re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '-', article_name).lower().replace(" ", "")[4:]):
                print(os.path.join(dst_path, "{}{}.pdf".format(article_name[:4], basename)))
                shutil.copyfile(path, os.path.join(dst_path, "{}{}.pdf".format(article_name[:4], basename)))
"""

file = glob("outputs/*/*.pdf")
flag = [False]*sum
for path in file:
    basename = os.path.basename(path)
    no = int(basename[:3])
    flag[no - 1] = True

f = open("not_found.txt", "w", encoding="utf-8")
idx = 0
for session, article_list in sessions_article_dict.items():
    f.write(session + "\n")
    for article in article_list:
        if not flag[idx]:
            print(article)
            f.write(article + "\n")
        idx += 1
    f.write("\n")
f.close()