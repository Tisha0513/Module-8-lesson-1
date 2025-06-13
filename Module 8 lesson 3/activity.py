height = float(input("enter your height in meter"))
weight = float(input("enter your weight in kg"))

bmi = weight / (height * height)

print("Your BMI is", bmi)

if(bmi < 18.5):
    print("You are underweight")

elif(bmi <= 24.9):
            print("You are healthy")

elif(bmi <= 29.9):
            print("You are overweight")

else: 
    print("You are extremely obese. You should follow a diet")