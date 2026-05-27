weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in cm:"))
gender = input("Enter your gender (M/F):").strip().lower()


bmi = weight / (height / 100) ** 2


if gender.lower() == "f":
    ideal_weight = 45.5 + 2.3 * ((height / 2.54) - 60)
    print("Your ideal weight is:", ideal_weight)
    gender_text = "Female"
else:
    ideal_weight = 50 + 2.3 * ((height / 2.54) - 60)
    print("Your ideal weight is:", ideal_weight)
    gender_text = "Male"

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
else:
    print("Overweight")

print("Gender:", gender_text)
print("BMI:", round(bmi, 2))
print("Ideal Weight:", round(ideal_weight, 2), "kg")
