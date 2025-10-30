#no1
def bmi_category(weight_kg: float, height_m: float) -> str:
    if height_m <= 0:
        return "Invalid height"
    bmi = weight_kg / (height_m * height_m)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        if bmi >= 40:
            return "Obese (Severely)"
        else:
            return "Obese (Moderately)"

print(bmi_category(60, 1.70))   
print(bmi_category(45, 1.70))   
print(bmi_category(90, 1.70))   
print(bmi_category(120, 1.70)) 


#no2
def electricity_bill(units: int) -> tuple:
    if units < 0:
        raise ValueError("Units must be non-negative")
    bill = 0
    remaining = units

    take = min(remaining, 100)
    bill += take * 500
    remaining -= take

    take = min(remaining, 100)
    bill += take * 1000
    remaining -= take

    if remaining > 0:
        bill += remaining * 2000

    bill += 50000

    if bill > 500000:
        discounted = int(bill * 0.9)
        return bill, discounted
    else:
        return bill, None

print(electricity_bill(80))
print(electricity_bill(150))
print(electricity_bill(250))
print(electricity_bill(1000))


#no3
def scholarship(acad: int, extra: int, income: int) -> str:
    if acad >= 85:
        if extra >= 80:
            if income < 5_000_000:
                return "Scholarship A (Full tuition)"
            else:
                return "Scholarship A (Half tuition)"
        else:
            return "Scholarship B"
    elif 70 <= acad <= 84 and extra >= 90:
        return "Scholarship C"
    else:
        return "No Scholarship"

print(scholarship(90, 85, 4_000_000))
print(scholarship(90, 85, 6_000_000))
print(scholarship(90, 70, 4_000_000))
print(scholarship(75, 95, 4_000_000))
print(scholarship(60, 70, 3_000_000))


#no4
def final_grade(exam: float, project: float) -> str:
    final = exam * 0.7 + project * 0.3
    grade = None
    if final >= 90:
        grade = "A"
    elif final >= 80:
        grade = "B"
    elif final >= 70:
        grade = "C"
    elif final >= 60:
        grade = "D"
    else:
        grade = "F"

    if grade == "B" and project >= 95:
        return "A (upgraded)"
    return grade

print(final_grade(90, 90))
print(final_grade(80, 85))
print(final_grade(80, 95))
print(final_grade(70, 70))
print(final_grade(50, 50))


#no5
def max_of_three(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

print(max_of_three(7, 12, 5))   
print(max_of_three(30, 10, 20)) 
print(max_of_three(15, 25, 40)) 


#no6
def banking_simulation(commands):
    """
    commands: list of tuples
      (1, amount) -> deposit
      (2, amount) -> withdraw
      (3,) -> check balance
      (4,) -> exit
      For withdraw > 500000, next command must be ('confirm', 'Y' or 'N') or ('confirm', )
    """
    balance = 1_000_000
    out = []
    i = 0
    while i < len(commands):
        cmd = commands[i]
        i += 1
        if cmd[0] == 1:
            amt = cmd[1]
            if amt <= 0:
                out.append("Invalid deposit amount")
            else:
                balance += amt
                out.append(f"Deposit successful, Balance = {balance:,}")
        elif cmd[0] == 2:
            amt = cmd[1]
            if amt > balance:
                out.append("Insufficient balance")
            else:
                if amt > 500_000:
                    if i < len(commands) and commands[i][0] == 'confirm':
                        confirmation = commands[i][1] if len(commands[i]) > 1 else 'N'
                        i += 1
                        if confirmation.upper() == 'Y':
                            balance -= amt
                            out.append(f"Withdraw successful, Balance = {balance:,}")
                        else:
                            out.append("Withdrawal cancelled")
                    else:
                        out.append("Confirmation required")
                else:
                    balance -= amt
                    out.append(f"Withdraw successful, Balance = {balance:,}")
        elif cmd[0] == 3:
            out.append(f"Balance = {balance:,}")
        elif cmd[0] == 4:
            out.append("Exit")
            break
        else:
            out.append("Invalid option")
    return out

commands = [
    (3,),                  
    (1, 200_000),          
    (2, 1_300_000),        
    (2, 600_000),          
    ('confirm', 'Y'),      
    (4,)                   
]

for line in banking_simulation(commands):
    print(line)


#no7
def ticket_price(age: int, membership: str, day_type: str) -> int:
    base = 100_000
    if day_type.lower() == "weekend":
        base += 20_000

    discounts = []
    if age < 12:
        discounts.append(0.50)
    if age >= 60:
        discounts.append(0.30)
    if membership.lower() in ("yes", "y", "true"):
        discounts.append(0.20)

    discount = max(discounts) if discounts else 0.0
    final_price = int(base * (1 - discount))
    return final_price

print(ticket_price(10, "No", "Weekday"))   
print(ticket_price(65, "No", "Weekday"))   
print(ticket_price(30, "Yes", "Weekday"))  
print(ticket_price(30, "No", "Weekend"))  
print(ticket_price(10, "Yes", "Weekend"))

#no8
def nth_from_second_difference(a1, a2, a3, a4, n):
    L0 = [a1, a2, a3, a4]
    if n <= len(L0):
        return L0[n-1]

    L1 = [L0[i+1] - L0[i] for i in range(len(L0)-1)]
    L2 = [L1[i+1] - L1[i] for i in range(len(L1)-1)]

    if not all(x == L2[0] for x in L2):
        raise ValueError("Not a 2-layer (constant second difference) sequence")

    const = L2[0]

    deep = [const]
    curr_L1 = L1[:]  # e.g. [2,8,14]
    curr_L0 = L0[:]  # e.g. [1,3,11,25]

    while len(curr_L0) < n:
        deep.append(const)
        next_l1_value = curr_L1[-1] + deep[-1]
        curr_L1.append(next_l1_value)
        next_l0_value = curr_L0[-1] + curr_L1[-1]
        curr_L0.append(next_l0_value)
    return curr_L0[n-1]

print(nth_from_second_difference(1,3,11,25,5))
print(nth_from_second_difference(1,3,11,25,6))
print(nth_from_second_difference(1,3,11,25,10))
print(nth_from_second_difference(2,5,10,17,7))



#BONUS
 

#BONUS2
def jug_problem():
    jug7, jug4 = 0, 0
    steps = []

    jug4 = 4
    steps.append((jug7, jug4))

    transfer = min(jug4, 7 - jug7)
    jug7 += transfer
    jug4 -= transfer
    steps.append((jug7, jug4))

    jug4 = 4
    steps.append((jug7, jug4))

    transfer = min(jug4, 7 - jug7)
    jug7 += transfer
    jug4 -= transfer
    steps.append((jug7, jug4))

    return steps

result = jug_problem()
for i, state in enumerate(result, 1):
    print(f"Step {i}: Jug7={state[0]}L, Jug4={state[1]}L")
