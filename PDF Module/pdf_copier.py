import PyPDF2


pdf1File = open('C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/Triada/PTD_Piston.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
	pageObj = pdf1Reader.getPage(pageNum)
	print(pageObj.getContents())
	print(type(pageObj))
	for i in pageObj:
		print(type(i),i)
	pdfWriter.addPage(pageObj)


pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()