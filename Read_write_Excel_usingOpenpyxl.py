import openpyxl

# Load workbook
wk=openpyxl.load_workbook("to_do_list.xlsx")
print(wk.sheetnames)
print("Acive sheet is",wk.active.title)

# Create object of any sheet you want to work on
sh=wk['Sheet1']
print(sh['C11'].value)




