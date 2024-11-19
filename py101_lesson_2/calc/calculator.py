"""This is a simple calculator that performs basic arithmetic operations."""


def prompt(message):
    """Prepend a prompt symbol to a message."""
    print(f'==> {message}')

def invalid_number(number_str):
    """Check if a string is a valid number."""
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt('What operation would you like to perform? \
    1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4.')
    operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

print(f"The result is: {output}")
