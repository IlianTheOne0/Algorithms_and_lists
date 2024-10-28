def main():
    try:
        print(finder(input('Enter the text: '), input('Enter the character you want to search for: ')))
    except Exception as e:
        print(f'Error: {e}')

def finder(text, char):
    pass