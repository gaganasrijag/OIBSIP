print("===== BMI CALCULATOR =====")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight/(height ** 2)

print("\nYour BMI is:", round(bmi,2))

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
    
print("Category:",category)

print("\nThank you for using the BMI Calculator!")
    
