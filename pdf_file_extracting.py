#!/usr/bin/python
import PyPDF2 as pdf

f = open("[Christophe_Jaffrelot,_Cynthia_Schoch]_The_Pakista(z-lib.org).pdf","rb")
pdfReader = pdf.PdfFileReader(f)

for i in range(pdfReader.getNumPages()):
    a = pdfReader.getPage(i).extractText()
    fil = open("page%s" % i,"w")
    fil.write(a)
    fil.close()


