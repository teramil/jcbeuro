import csv
import xlrd

found_counter = 0


def GetListOfSKUFromPriceList(SKUStr):
	SKUList = []
	if "," in SKUStr:
		SKUList.extend(SKUStr.split(","))
		for i in range(len(SKUList)):
			SKUList[i] = SKUList[i].replace(" ", "")
	elif " " in SKUStr:
		SKUList.extend(SKUStr.split(" "))
	else:
		SKUList.append(SKUStr)

	SKUList = [x for x in SKUList if x]
	return SKUList


def GetPriceBySKU(file, sku):
	print(sku)
	
	p_book = xlrd.open_workbook(file)
	
	sheet1 = p_book.sheet_by_index(1)
	sheet2 = p_book.sheet_by_index(2)

	for rownum in range(sheet1.nrows):
		row = sheet1.row_values(rownum)
		for i in GetListOfSKUFromPriceList(row[0]):
			if sku == i:
				return row[3]

	for rownum in range(sheet2.nrows):
		row = sheet2.row_values(rownum)
		for i in GetListOfSKUFromPriceList(row[0]):
			if sku == i:
				return row[3]

	global found_counter
	found_counter+=1
	return None


def main():
	
	global found_counter
	
	catalog_file = "jcbeuro_ru.csv"
	new_catalog_file = "jcbeuro_ru_new.csv"
	log_file_path = "log.txt"
	prices_file = "sorted_prices.xlsx"

	c_file = open(catalog_file, "r")
	c_reader = csv.DictReader(c_file)
	nc_file = open(new_catalog_file, "w")
	log_file = open(log_file_path, "w")
	c_writer = csv.DictWriter(nc_file, c_reader.fieldnames)

	c_writer.writeheader()

	for line in c_reader:
		if line["SKU"]:
			log_file.write("----------------------------------\n")
			log_file.write("Артикул: " + line["SKU"] + "\n")
			log_file.write("Новая цена: ")

			newline = line["SKU"].split(",")
			newprice = GetPriceBySKU(prices_file, newline[0])
			
			if newprice:
				line["Price"] = newprice
				log_file.write(str(newprice)+"\n")
			else:
				log_file.write("Not found\n")

			log_file.write("\n")

		c_writer.writerow(line)
		
	log_file.write("\n")
	log_file.write("======================================\n")
	log_file.write("Не найдено: " + str(found_counter))


def test():
	print(GetListOfSKUFromPriceList("12312   3456"))


if __name__ == "__main__":
	main()
	#test()
