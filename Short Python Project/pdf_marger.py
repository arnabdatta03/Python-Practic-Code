import pyPDF2
pdf_files = []
pdf_count = int(input("Enter How Many Pdf You Marged: "))
for i in range(pdf_count):
    pdf_name = input("Enter The Name Of Pdf {}:".format(i+1))
    list.append(pdf_name)
print("User input list:", pdf_files)
marger=pyPDF2.PdfMerger()
for filename in pdf_files:
    pdf_files = open(filename,'rb')
    pdfReader = pyPDF2.PdfReader(pdf_files)
    marger.append(pdfReader)
pdf_files.close()
marger.write("Merged Pdf")
