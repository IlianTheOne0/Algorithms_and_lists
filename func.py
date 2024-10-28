def main():
    print('The number of times the symbol is repeated:', finder(input('Enter the text: '), input('Enter the character you want to search for: ')))

def finder(text, char):
    result = 0

    for i in text:
        if i == char:
            result += 1

    return result