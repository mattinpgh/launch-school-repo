"""This is a simple calculator that performs basic arithmetic operations."""
import json


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

with open('calc.config.json', 'r') as file:
    data = json.load(file)

prompt(data['messages']['welcome'])

while True:
    prompt(data['messages']['check_1'])
    number1 = input()

    while invalid_number(number1):
        prompt(data['messages']['invalid_number'])
        number1 = input()

    prompt(data['messages']['check_2'])
    number2 = input()

    while invalid_number(number2):
        prompt(data['messages']['invalid_number'])
        number2 = input()

    prompt(data['messages']['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(data['messages']['operation_check'])
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
    if not input(data['messages']['run_again']).lower().startswith('y'):
        break
