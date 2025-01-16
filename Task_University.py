# # from openpyxl import workbook , load_workbook

# # wb = workbook()
# # ws = wb.active
# # ws.title = 'yaska'

# # ws['A1'] = 34
# # ws['A2'] = 90
# # ws['A3'] = 98
# # ws['A4'] = 91
# # ws['A5'] = 90
# # if ws ==8

# # from openpyxl import Workbook


# # # Write data to the sheet
# # ws['A1'] = "Name"
# # ws['B1'] = "Age"
# # ws['A2'] = "Alice"
# # ws['B2'] = 60
# # ws['A3'] = "Bob"
# # ws['B3'] = 99

# # # Save the workbook
# # wb.save("example.xlsx")
# # print("File 'example.xlsx' created.")

# # for row in range(1,ws.max_row+1):
# #     if ws.cell(row=row , column=1).value==60:
# #         ws.cell(row=row , column=2 , value='PASS')
# #     else:  
# #         continue  

# # # *2. Read data from the Excel file*
# # wb = load_workbook("example.xlsx")  # Load the workbook
# # ws = wb.active  # Get the active sheet

# # # Read specific cells
# # print(f"Cell A1: {ws['A1'].value}")
# # print(f"Cell B2: {ws['B2'].value}")

# # # Iterate through rows and print data
# # print("\nAll Data:")
# # for row in ws.iter_rows(min_row=1, max_row=3, values_only=True):
# #     print(row)

# # # *3. Modify the existing Excel file*
# # ws['B2'] = 26  # Update Alice's age
# # ws.append(["Charlie", 35])  # Add a new row

# # # Save changes
# # wb.save("example.xlsx")
# # print("\nFile updated with new data.")


# from openpyxl import Workbook

# # Create a new workbook
# wb = Workbook()
# ws = wb.active
# ws.title = "Student Performance Report"

# # Define headers
# headers = ["Student Name", "Math", "Science", "English", "Total", "Average", "Grade"]

# # Write headers
# for col, header in enumerate(headers, 1):
#     ws.cell(row=1, column=col, value=header)

# # Sample student data
# student_data = [
#     ["Yasin", 35, 22, 98],
#     ["Omar", 95, 88, 90],
#     ["Michael Brown", 72, 75, 80],
#     ["Sarah Davis", 58, 15, 92],
#     ["James Johnson", 65, 70, 68]
# ]

# # Write student data and calculate totals, averages, and grades
# for row, student in enumerate(student_data, 2):
#     # Write basic data
#     for col, value in enumerate(student, 1):
#         ws.cell(row=row, column=col, value=value)
    
#     # Calculate total (sum of Math, Science, English)
#     total = sum(student[1:])
#     ws.cell(row=row, column=5, value=total)
    
#     # Calculate average
#     average = total / 3
#     ws.cell(row=row, column=6, value=round(average, 2))
    
#     # Determine grade
#     if average >= 60:
#         grade = 'PASS'
#     else:
#         grade = 'FAIL'
    
#     ws.cell(row=row, column=7, value=grade)

# # Adjust column widths (basic adjustment)
# for col in range(1, 8):
#     ws.column_dimensions[chr(64 + col)].width = 15

# # Save the workbook
# wb.save("Student_Performance_Report.xlsx")
# print("Student Performance Report has been created successfully!")

number= 23,3232,32,3,2
# for index, i in enumerate(number,1):
#     print(index , i)
#  lists contain 9 trees
rabbit = [
    ['4🌲','🌲','🌲'],
    ['here🌲','🌲','🌲'],
    ['🌲','🌲','🌲'],
]
rabbit[1][0] ='ff'
print(rabbit)
