def atbash(txt):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse = alphabet[::-1]

    _map = {alphabet[index]: reverse[index] for index in range(len(alphabet))}
    
    result = []

    for letter in txt:
        result.append(_map[letter])
    
    return print(''.join(result))


# for test
atbash(txt='thisisatest')
