#!/usr/bin/python

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
		for r, row in enumerate(reader):
			totalColumn += 1
			for c, col in enumerate(row):
				# convert strings into integers from certain column
				if (r != 0 and c in range(2,5) and col != ''):
					worksheet.write_number(r, c, float(col))
	
					# hide rows that don't match the filter.
					if c == 2 and float(col) < float(limit):
						worksheet.set_row(r, options={'hidden': True})
				else:
					worksheet.write(r, c, col)
	
	# Set the autofilter.
	worksheet.autofilter('C2:C' + str(totalColumn))
	worksheet.filter_column('C', 'x > ' + limit)
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
