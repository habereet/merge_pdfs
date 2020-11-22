import os
from PyPDF2 import PdfFileMerger

loc = "basepdfs/"

files = sorted(os.listdir(loc)) 
files = [file for file in files if file.endswith(".pdf")]

merger = PdfFileMerger()
for pdf in files:
    merger.append(open(f'basepdfs/{pdf}','rb'))
with open("result.pdf", "wb") as fout:
    merger.write(fout)