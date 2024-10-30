def main():
    print('The number of times the word is repeated:', finder(input('Enter the text: '), input('Enter the word you want to search for: ')))

def spliter(text) -> list:
    pattern = '.,!?@#$%^&*()_+'

    for char in pattern:
        text = text.replace(char, '')

    return text.lower().split()

def finder(text, word) -> int:
    result = 0

    for i in spliter(text):
        if i == word.lower():
            result += 1

    return result