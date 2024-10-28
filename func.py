def main():
    try:
        print('The number of times the symbol is repeated:', finder(input('Enter the text: '), input('Enter the character you want to search for: ')))
    except Exception as e:
        print(f'Error: {e}')

def finder(text, char):
    result = 0

    for i in text:
        if i == char:
            result += 1

    return result