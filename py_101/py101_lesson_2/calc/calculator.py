"""This is a simple calculator that performs basic arithmetic operations."""
import json


def prompt(message):
    """Prepend a prompt symbol to a message."""
    print(f'==> {message}')

def invalid_number(number_str):
    """Check if a string is a valid number."""
    try:
        float(number_str)
    except ValueError:
        return True

    return False

with open('calc.config.json', 'r') as file:
    data = json.load(file)

prompt('Select your language: 1. English, 2. Spanish, 3. French: ')
language = input()
if language == '1':
    lang_messages = "english_messages"
elif language == '2':
    lang_messages = "spanish_messages"
elif language == '3':
    lang_messages = "french_messages"
else:
    prompt('Invalid language selection. Please try again.')
    exit(1)

prompt(data[lang_messages]['welcome'])

while True:
    prompt(data[lang_messages]['check_1'])
    number1 = input()

    while invalid_number(number1):
        prompt(data[lang_messages]['invalid_number'])
        number1 = input()

    prompt(data[lang_messages]['check_2'])
    number2 = input()

    while invalid_number(number2):
        prompt(data[lang_messages]['invalid_number'])
        number2 = input()

    prompt(data[lang_messages]['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(data[lang_messages]['operation_check'])
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    print(f"The result is: {output}")
    if not input(data[lang_messages]['run_again']).lower().startswith('y'):
        break
