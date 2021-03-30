import xlrd
def parse_file(filename):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(row, col) for col in range(sheet.ncols)] for row in range(sheet.nrows)]

    print('\nList Comprehension')
    print('data[1][2]:')
    print(data[1][2])

    print('\nCells in a nested loop:')
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 10:
                print(sheet.cell_values(row, col))

    print('\nRows, Columns, and Cells:')
    print('Numbers of rows in the sheet:')
    print(sheet.nrows)

    print('Type of data in cell(row3,col2):')
    print(sheet.cell_type(3, 2))

    print('Value in cell(row3,col2):')
    print(sheet.cell_value(3, 2))

    print('Get a slice of values in column3, from rows 1-3:')
    print(sheet.col_values(3, start_rowx=1, end_rowx=4))  #This will return a list

    print('\nDates:')
    print('Type of data in cell(row1,col0):')
    print(sheet.cell_type(1, 0))

    exceltime = sheet.cell_value(1, 0)
    print('Time in Excel Format:')
    print(exceltime)

    print('Convert time to a python datetime tuple from the excel float:')
    print(xlrd.xldate_as_tuple(exceltime, 0))

    return data
