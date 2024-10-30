def main():
    try:
        # print('The number of times the word is repeated:', finder(input('Enter the text: '), input('Enter the word you want to search for: ')))
        print(finder('Hello world hello world world hello World hello Wello Horld', 'world'))
    except Exception as e:
        print(f'Error: {e}')

# Function to find the number of times a word is repeated in a text

def replacer() -> str:
    pass

def finder(text, word) -> int:
    return text.lower().split().count(word.lower())