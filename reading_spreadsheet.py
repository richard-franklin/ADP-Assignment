import xlrd

wb = xlrd.open_workbook("sample.xls")
sheet = wb.sheet_by_index(0)

print("\nNumber of rows : ",sheet.nrows)
print("\nNumber of columns : ",sheet.ncols)

print("\nThe column names : ",[sheet.cell_value(0, i) for i in range(sheet.ncols) ])

print("\n The first column values : ",[sheet.cell_value(i, 0) for i in range(sheet.nrows)])

print("\nValue of first row : ",sheet.row_values(1))