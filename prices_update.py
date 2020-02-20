import csv
import xlrd


def GetPriceBySKU(file, sku):
	
	print(sku)
	
	p_book = xlrd.open_workbook(file)
	
	sheet1 = p_book.sheet_by_index(1)
	sheet2 = p_book.sheet_by_index(2)

	for rownum in range(sheet1.nrows):
		row = sheet1.row_values(rownum)
		if sku in row[0]:
			print(row)
			return row[3]

	for rownum in range(sheet2.nrows):
		row = sheet2.row_values(rownum)
		if sku in row[0]:
			print(row)
			return row[3]
	return null


def main():
	catalog_file = "jcbeuro_ru.csv"
	new_catalog_file = "jcbeuro_ru_new.csv"

	prices_file = "sorted_prices.xlsx"

	c_file = open(catalog_file, "r")
	reader = csv.DictReader(c_file)

	nc_file = open(new_catalog_file, "w")

	print(GetPriceBySKU(prices_file, "320/04208"))


if __name__ == "__main__":
	main()
