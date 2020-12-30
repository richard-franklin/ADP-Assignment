import xlwt
from xlwt import Workbook

wb = Workbook() 

sheet1 = wb.add_sheet('Sheet 1') 

sheet1.write(0,0,'USN')
sheet1.write(0,1,'Name')
sheet1.write(0,2,'Marks')
sheet1.write(1,0,'121')
sheet1.write(1,1,'Chris')
sheet1.write(1,2,'100')
sheet1.write(2,0,'122')
sheet1.write(2,1,'Erik')
sheet1.write(2,2,'99')
sheet1.write(3,0,'123')
sheet1.write(3,1,'Evans')
sheet1.write(3,2,'89')
sheet1.write(4,0,'124')
sheet1.write(4,1,'Laura')
sheet1.write(4,2,'100')
sheet1.write(5,0,'125')
sheet1.write(5,1,'Sheltear')
sheet1.write(5,2,'69')

wb.save('xlwt example.xls') 
print("Excel file created")