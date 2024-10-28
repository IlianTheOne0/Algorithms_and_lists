def main():
    print('Inverted text:', inverter(str(input('Enter the text: '))))

def _len(data):
    number = 0

    for temp in data:
        number += 1

    return number

def inverter(text):
    length = _len(text)
    result = str()

    for i in range(length):
        result += str(text[length - i - 1])

    return result