def main():
    print('Inverted text:', inverter(input('Enter the text: ')))

def _len(data) -> int:
    number = 0

    for temp in data:
        number += 1

    return number

def inverter(text) -> str:
    length = _len(text)
    result = str()

    for i in range(length):
        result += str(text[length - i - 1])

    return result