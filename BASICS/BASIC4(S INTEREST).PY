# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


principal_amount = int(input("Enter the principal amount: "))
interest_rate = int(input("Enter the annual interest rate (%): "))
time_period = int(input("Enter the time period (in years): "))

simple_interest = calculate_simple_interest(principal_amount, interest_rate, time_period)

print(f"Simple Interest for principal ${principal_amount}, interest rate {interest_rate}%, and time {time_period} years is:₹{simple_interest}")
