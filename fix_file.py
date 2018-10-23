import xlrd
import xlwt

workbook = xlrd.open_workbook('epi_r.xls', encoding_override="utf8")
worksheet = workbook.sheet_by_index(0)
row = worksheet.nrows
col = worksheet.ncols

data = []

for x in range(0, row):
    data.append([])
    for y in range(0, col):
        data[x].append(worksheet.cell(x, y).value)

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=True)

for i in range(0, len(data[0])):
    sheet1.write(0, i, data[0][i])

rowsum = 0
x_counter = 1

for x in range(1, len(data)):
    for y in range(1, len(data[x])):
        rowsum = rowsum + int(data[x][y])
    if rowsum > 3:
        for y2 in range(0, len(data[x])):
            sheet1.write(x_counter, y2, data[x][y2])
        x_counter = x_counter + 1

    rowsum = 0

book.save("new_epi_r.xls")




