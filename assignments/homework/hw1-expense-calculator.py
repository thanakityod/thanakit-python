monthly_income = float(input("monthly income (THB): "))
rent_cost = float(input("Monthly rent/housing cost: "))
food_budget = int(input("Monthly food budget in (THB): "))
transportation_cost = float(input("Monthly transportation expenses: "))
entertainment_budget = int(input("Monthly entertainment budget: "))
emergency_fund_percent = float(input("Percentage to save for emergency (e.g., 10.5): "))
investment_percent = float(input("Percentage to invest (e.g., 15.0): "))

Total_Fixed_Expenses = rent_cost + transportation_cost
Total_Variable_Expenses = food_budget + entertainment_budget
Total_Expenses = Total_Fixed_Expenses + Total_Variable_Expenses
Remaining_Income = monthly_income - Total_Expenses
Emergency_Fund_Amount = monthly_income * (emergency_fund_percent / 100)
Investment_Amount = monthly_income * (investment_percent / 100)
Available_for_Savings = Remaining_Income - Emergency_Fund_Amount - Investment_Amount

Expense_Ratio = (Total_Expenses / monthly_income ) * 100

print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {Total_Fixed_Expenses:.2f} THB")
print(f"Variable Expenses: {Total_Variable_Expenses:.2f} THB")
print(f"Total Expenses: {Total_Expenses:.2f} THB")
print(f"Remaining: {Remaining_Income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%): {Emergency_Fund_Amount:.2f} THB")
print(f"Investment ({investment_percent}%): {Investment_Amount:.2f} THB")
print(f"Available for Savings: {Available_for_Savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {Expense_Ratio:.2f}%") 