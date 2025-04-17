working_days = int(input("enter the number of working days: "))
absent_days = int(input("enter the number of days you were absent: "))
attendance_percentage = (working_days - absent_days) * 100 / working_days
if attendance_percentage > 75:
    print("you are eligible to write the exam")
else:
    print("you are not eligible to write the exam")
