def main():
    numbers, letters = counter(input('Enter the text: '))
    print(f'Amount of letters: {letters}\nAmount of numbers: {numbers}')

def counter(text) -> tuple:
    amount_of_numbers = 0
    amount_of_letters = 0

    pattern_of_symbols = r" [',.:/\\!@#$%^&*()_+{}\[\];\"<>?|`~\-]"

    for i in text:
        if '9' >= i >= '0':
            amount_of_numbers += 1
        elif i not in pattern_of_symbols:
            amount_of_letters += 1

    return amount_of_numbers, amount_of_letters