def caesar(txt, shift, type):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sub = alphabet[shift:] + alphabet[:shift]

    if type == 'e': # for encrypt
        _map = {alphabet[index]: sub[index] for index in range(len(alphabet))}
    elif type == 'd': # for decrypt
        _map = {sub[index]: alphabet[index] for index in range(len(alphabet))}
    result = []

    for letter in txt:
        result.append(_map[letter])

    return print(''.join(result))


caesar(txt='test', shift=5, type='e')
caesar(txt='yjxy', shift=5, type='d')
