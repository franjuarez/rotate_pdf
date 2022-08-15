from pdfrw import PdfReader, PdfWriter
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

def pages_number_input():
	pages_number = input(
		"Which pages do you want to rotate?\nRemember that this will turn one every two pages. The first page will be the first turned around\nExample: 1-20")
	first_page, last_page = map(int, pages_number.split('-'))
	if pages_number and first_page > last_page:
		say("The last page can't be higher than the first page!")
		return
	return pages_number


def rotation_input():
	rotation = input('How many clockwise degrees do you want to rotate it?\nIt should be a multiple of 90')
	if rotation and (not rotation.isnumeric() or int(rotation) % 90 != 0) : #in case they don't write a number or a valid numbe one
		say("This isn't a valid angle! Remember it should be a multiple of 90")
		return
	return rotation

def rotation_number_input():
	rotation_number = input('Every how many pages do you want to rotate?')
	if rotation_number and (not rotation_number.isnumeric() or int(rotation_number) <= 0):
		say('It has to be a positive number!')
		return
	return rotation_number

def write_rotated_pdf(file, pages, rotation, pages_number, rotation_number):
	writer = PdfWriter()

	first_page, last_page = map(int, pages_number.split('-'))
	rotation_rest = (first_page-1) % rotation_number
	for page_number, page in enumerate(pages):
		if page_number < (first_page-1) or page_number >= last_page:
			writer.addpage(page)
			continue
		if page_number % rotation_number == rotation_rest:
			page.Rotate = (int(page.inheritable.Rotate or 0) + rotation) % 360
		writer.addpage(page)

	with open(f"new_{file}","wb") as nuevo:
		writer.write(nuevo)

def main():
	title('PDF Straighten')
	file_name = pdf_input()
	pages = valid_file(file_name)
	if not pages: return
	pages_number = pages_number_input()
	if not pages_number: return
	rotation = rotation_input()
	if not rotation: return
	rotation_number = rotation_number_input()
	if not rotation_number: return
	write_rotated_pdf(file_name, pages, int(rotation), pages_number, int(rotation_number))

init(main)
