
total_days = int(input("Enter total number of working days: "))
absent_days = int(input("Enter total number of days absent: "))


attended_days = total_days - absent_days


percentage = (attended_days / total_days) * 100


print("Attendance percentage:", percentage)


if percentage < 75:
    print("You are not allowed to sit in the exam.")
else:
    print("You are allowed to sit in the exam, ")
