#Day 2
#Data types
#String
print("Hello"[0])
"Hello"[4]
print("hello" + "world")
#interger
print(123 + 345)
#float
3.124
#Boolean
True
False
num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("your name has" + new_num_char + "characters.")

a = float(123)
print(type(a))
print(str(70) + str(100))
   #exercise
two_digit_number = input("type a two digit number")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)

#PEMDASLR
#(),**,*,/,+,-
print(3 * 3 + 3 / 3 - 3)
      #BMI CALCULATOR
heigth = input("enter your height in m:")
weight = input("enter your weight in kg:")
bmi = int(weight) / float(heigth) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
print(round(8 / 3, 2))
score = 0
heigth = 1.8
isWinning = True
  #f_string
print(f"your score is {score}, your height is {heigth}, you are winning is {isWinning}")

  #exercise
age = input("what is your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months."
print(message)


        #FINAL PROJECT
print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15?"))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount} ")
