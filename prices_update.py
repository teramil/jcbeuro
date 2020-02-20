import csv
import xlrd


def GetPriceBySKU(file, sku):
	p_book = xlrd.open_workbook(file, formatting_info=True)
	sheet1 = p_book.sheet_by_index(1)
	sheet2 = p_book.sheet_by_index(2)
	for row in sheet1:
		if sku in row[0]:
			return row[3]

	for row in sheet2:
		if sku in row[0]:
			return row[3]
	return null


def main():
	catalog_file = "jcbeuro_ru.csv"
	new_catalog_file = "jcbeuro_ru_new.csv"

	prices_file = "sorted_prices.xlsx"

	c_file = open(catalog_file, "r")
	reader = csv.DictReader(c_file)

	nc_file = open(new_catalog_file, "w")
	

if __name__ == "__main__":
	main()
