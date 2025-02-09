import openpyxl

# Load the workbook and select the active worksheet
wb = openpyxl.load_workbook('../data/iris/iris dataset.xlsx')
sheet = wb.active

# Get the range B4 to B10
cells = sheet['B4:B10']

# Extract the values into a list
values = [cell[0].value for cell in cells]

# Display the values
print(values)