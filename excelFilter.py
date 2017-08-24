#!/usr/bin/python

HEADER_DIFFIMPEDANCE = "Diff Impedance (Ohm)"
HEADER_LENGTH = "Length (mil)"
HEADER_TRACEDELAY = " Trace Delay (ps)"

def excelFilter(path, limit):
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
		INDEX_DIFFIMPEDANCE = row1.index(HEADER_DIFFIMPEDANCE)
		INDEX_LENGTH = row1.index(HEADER_LENGTH)
		INDEX_TRACEDELAY = row1.index(HEADER_TRACEDELAY)

		for r, row in enumerate(reader):
			totalColumn += 1
			for c, col in enumerate(row):
				# convert strings into integers from certain column
				if (r != 0 and c in [INDEX_DIFFIMPEDANCE, INDEX_LENGTH, INDEX_TRACEDELAY] and col != ''):
					worksheet.write_number(r, c, float(col))
	
					# hide rows that don't match the filter.
					if c == INDEX_DIFFIMPEDANCE and float(col) < float(limit):
						worksheet.set_row(r, options={'hidden': True})
				else:
					worksheet.write(r, c, col)

	
	# Set the autofilter.
	worksheet.autofilter(2-1, INDEX_DIFFIMPEDANCE, totalColumn-1, INDEX_DIFFIMPEDANCE) # ps: -1 due to the index begin from 0
	worksheet.filter_column(INDEX_DIFFIMPEDANCE, 'x > ' + limit)
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
	if(os.path.exists(path)):
		excelFilter(path, limit)
	else:
		print "file not exist!"

if __name__ == '__main__':
    main()
