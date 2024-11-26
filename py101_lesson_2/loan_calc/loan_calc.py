"""Main module. Calculates monthly payments"""


def monthly_payment(loan_amount, apr, duration_in_years):
    """Calculates monthly payment for loan. Returns a string.
    loan_amount: loan amount in dollars
    apr: annual percentage rate expressed as a decimal
    duration_in_years: loan duration in years"""
    if apr > 1:
        apr /= 100

    monthly_interest_rate = apr / 12
    loan_duration_in_months = duration_in_years * 12

    monthly_payment = loan_amount * (monthly_interest_rate /
                        (1 - (1 + monthly_interest_rate) **  (-loan_duration_in_months)))
    return f"${monthly_payment:,.2f}"

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
        if float(number_str) <= 0:
            raise ValueError("The value must be greater than 0.")
    except ValueError:
        return True

    return False

while True:
    prompt("Welcome to the mortgage/loan calculator.")
    prompt("Please enter the loan amount:")
    loan_amount = input()
    while invalid_number(loan_amount):
        prompt("Invalid loan amount. Please enter a valid number:")
        loan_amount = input()

    prompt("Please enter the annual percentage rate, expressed as a decimal:")
    apr = input()
    while invalid_number(apr):
        prompt("Invalid annual percentage rate. Please enter a valid number:")
        apr = input()

    prompt("Please enter the duration of the loan in years - decimals to represent"
           "partial years are acceptable:")
    duration_in_years = input()
    while invalid_number(duration_in_years):
        prompt("Invalid duration of loan. Please enter a valid number:")
        duration_in_years = input()

    m_payment = monthly_payment(
                        loan_amount=float(loan_amount),
                        apr=float(apr),
                        duration_in_years=float(duration_in_years))

    prompt(f"Your monthly payment is: ${m_payment}")
    prompt("Would you like to perform another operation? (yes, no)")
    if input().lower().startswith('n'):
        prompt("Thank you for using the loan calculator.")
        break
