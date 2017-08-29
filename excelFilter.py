#!/usr/bin/python

def excelFilter(path, limit, filter_name):
	import csv
	from xlsxwriter.workbook import Workbook
	csvfile = path
	outfile = csvfile[:-3] + 'xlsx'

	totalColumn = 0

	workbook = Workbook(outfile)
	worksheet = workbook.add_worksheet()
	
	with open(csvfile, 'rt') as f:
		reader = csv.reader(f)

		# find the index of the column which we care about
		row1 = next(reader)
		for c, col in enumerate(row1):
			worksheet.write(0, c, col)
		INDEX_FILTER = row1.index(filter_name)

		for r, row in enumerate(reader):
			totalColumn += 1
			for c, col in enumerate(row):
				# convert strings into integers from certain column
				try:
					worksheet.write_number(r+1, c, float(col))
					# hide rows that don't match the filter.
					if c == INDEX_FILTER and float(col) < float(limit):
						worksheet.set_row(r+1, options={'hidden': True})
				except ValueError:
					worksheet.write(r+1, c, col)
	
	# Set the autofilter.
	worksheet.autofilter(1, INDEX_FILTER, totalColumn-1, INDEX_FILTER) # ps: -1 due to the index begin from 0
	worksheet.filter_column(INDEX_FILTER, 'x > ' + limit + ' or x == Blanks')
	workbook.close()

def main():
	import sys, os
	try:
		path = sys.argv[1]
		limit = sys.argv[2]
	except:
		print "Argument Error!"
		print "Usage: " + sys.argv[0] + " [path of *.csv] [filter number]"
		return

	try:
		filter_name = sys.argv[3]
	except:
		filter_name = "Diff Impedance (Ohm)"

	if(os.path.exists(path)):
		excelFilter(path, limit, filter_name)
	else:
		print "file not exist!"

if __name__ == '__main__':
    main()
