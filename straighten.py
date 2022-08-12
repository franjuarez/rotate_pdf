from pdfrw import PdfReader, PdfWriter, PageMerge
from gamelib import say, title, init, input

def pdf_input():
	file = input('Please write the name of the PDF you want to rotate.\nRemember that the PDF must be in the same folder as this program')
	if file and not file.lower().endswith('.pdf'): #in case they don't write '.pdf' or write it in uppercase
		return file + '.pdf'
	return file

def valid_file(file_name):
	if not file_name: return
	try:
		pages = PdfReader(file_name).pages #ain't CaseSensitive :)
	except:
		say("Not a valid PDF!")
		return
	return pages

def rotation_input():
	rotation = input('How many clockwise degrees do you want to rotate it?\nIt should be a multiple of 90')
	if rotation and (not rotation.isnumeric() or int(rotation) % 90 != 0) : #in case they don't write a number or a valid numbe one
		say("This isn't a valid angle! Remember it should be a multiple of 90")
		return
	return rotation

def write_rotated_pdf(file, pages, rotation):
	writer = PdfWriter()

	for i, page in enumerate(pages):
		if i % 2 != 0:
			page.Rotate = (int(page.inheritable.Rotate or 0) + rotation) % 360
		writer.addpage(page)

	with open(f"new_{file}","wb") as nuevo:
		writer.write(nuevo)

def main():
	title('PDF Straighten')
	file_name = pdf_input()
	pages = valid_file(file_name)
	if not pages: return
	rotation = rotation_input()
	if not rotation: return
	write_rotated_pdf(file_name, pages, int(rotation))

init(main)
