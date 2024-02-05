# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time, n):
    # Formula for compound interest: A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate / n) ** (n * time)
    compound_interest = amount - principal
    return compound_interest

principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (%): "))
time_period = float(input("Enter the time period in years: "))
compounding_frequency = int(input("Enter the compounding frequency per year: "))

compound_interest = calculate_compound_interest(principal_amount, interest_rate/100, time_period, compounding_frequency)

print(f"Compound Interest for principal ₹{principal_amount}, interest rate {interest_rate}%, time {time_period} years, and compounding frequency {compounding_frequency} times per year is: ₹{compound_interest:.2f}")
