def main():
    try:
        # print('The number of times the word is repeated:', finder(input('Enter the text: '), input('Enter the word you want to search for: ')))
        print(finder('Hello world hello world world hello World hello Wello Horld', 'world'))
    except Exception as e:
        print(f'Error: {e}')

def finder(text, word):
    result = 0

    for temp in text:
        if word == temp:
            result += 1

    return result