def main():
    try:
        print('Result:', calc(*input('Enter the math expression, separated with space: ').split(' ')))
    except Exception as e:
        print(f'Error: {e}')

def calc(first_number, operator, second_number) -> int:
    first_number, second_number = int(first_number), int(second_number)

    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        return first_number / second_number
    else:
        raise ValueError(f'unsupported operator {operator}')