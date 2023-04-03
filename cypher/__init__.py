import cr3.buggy as buggy

from pycipher import Caesar, Autokey, Atbash


log = buggy.log


def base6(string):

    key = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yz']
    try:
        string2 = int(string)
        word = ''
        for pair in range(0, len(string), 2):

            k = string[pair:pair+2]
            a = int(k[0])
            b = int(k[1])
            word += key[a][b]
        return word
    except ValueError:
        key = {
                'a': '00',
                'b': '01',
                'c': '02',
                'd': '03',
                'e': '04',
                'f': '05',
                'g': '10',
                'h': '11',
                'i': '12',
                'j': '13',
                'k': '14',
                'l': '15',
                'm': '20',
                'n': '21',
                'o': '22',
                'p': '23',
                'q': '24',
                'r': '25',
                's': '30',
                't': '31',
                'u': '32',
                'v': '33',
                'w': '34',
                'x': '35',
                'y': '40',
                'z': '41',
            }
        new_word = ''
        for each in string:
            new_word += key[each]
        return new_word


def phone(string, encode=False):
    key = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    if encode:
        string = list(string.lower())
        output = ''
        for char in string:
            for i in range(len(key)):
                if char in key[i]:
                    output += str(i) * (key[i].index(char)+1) + '0'
        output = output[:-1]
    else:
        string = string.split('0')
        output = ''
        for each in string:
            output += str(key[int(each[0])][len(each)-1])
    log.info(output)
    return output


def shift(string, key, encode=False):
    key = int(key)
    if encode:
        return Caesar(key).encipher(string).lower()
    else:
        return Caesar(key).decipher(string).lower()


def flip(string, encode=False):
    if encode:
        return Atbash.encipher(string).lower()
    else:
        return Atbash.decipher(string).lower()


def remove(string):
    return string.replace(' ', '')


def run(to_encrypt:str, code:str):
    to_encrypt = remove(to_encrypt)
    steps = code.split('\n')

    for step in steps:
        breakdown = step.split(' ')
        log.debug(breakdown)
        if breakdown[0] == 'base6':
            to_encrypt = base6(to_encrypt)
        elif breakdown[0] == 'flip':
            to_encrypt = flip(to_encrypt)
        elif breakdown[0] == 'shift':
            if len(breakdown) >= 2:
                to_encrypt = shift(to_encrypt, breakdown[1])
        elif breakdown[0] == 'phone':
            to_encrypt = phone(to_encrypt)

    return to_encrypt


if __name__ == '__main__':
    string = 'Hello'
    string = phone(string, True)
    string = phone(string)
