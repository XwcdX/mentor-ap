# 1. Triangle Type Checker
a, b, c = 3, 4, 5
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# 2. Grade Converter
score = 85
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")


# 3. ATM Withdrawal Validator
amount = 145
if amount % 50 == 0:
    print("OK")
else:
    print("Invalid amount")


# 4. Leap Year Checker
year = 2024
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not leap year")


# BONUS: Days to Years, Months, Days
days = 800
years = days // 365
remaining_days = days % 365
months = remaining_days // 30
remaining_days = remaining_days % 30

print(f"{years} years, {months} months, {remaining_days} days")
