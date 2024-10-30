def main():
    print('Your restructured text:', replacer(input('Enter the text: '), input('Enter the word you want to replace: '), input('Enter the word you want to replace with: ')))

def spliter(text) -> list:
    pattern = '.,!?@#$%^&*()_+'

    for char in pattern:
        text = text.replace(char, '')

    return text.lower().split()

def replacer(text, to_replace, how_to_replace) -> str:
    for i in spliter(text):
        if i == to_replace.lower():
            text = text.replace(i, how_to_replace)

    return text