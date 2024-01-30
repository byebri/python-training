height = float(input())
weight = int(input())
bmi = weight / (height * height)
if bmi < 18.5:
  x = (" you are underweight.")
elif bmi < 25:
  x = (" you have a normal weight.")
elif bmi < 30:
  x = (" you are slightly overweight.")
elif bmi < 35:
  x = (" you are obese.")
else:
  x = (" you are clinically obese.")
print(f"Your BMI is {bmi}," + x)
