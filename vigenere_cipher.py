def vigenere(text, key, type):
    text = text.replace(' ', '')
    key = key.replace(' ', '')
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    vigenereList = []

    for index in range(len(alphabet)):
        vigenereList.append(alphabet[index:] + alphabet[:index])

    result = []

    for j in range(len(text)):
        for i in vigenereList:
            if i[0] == key[j]:
                _map = i
                if type == 'e': # for encrypt
                    mapped = {alphabet[k]: _map[k] for k in range(len(alphabet))}
                elif type == 'd': # for decrypt
                    mapped = {_map[k]: alphabet[k] for k in range(len(alphabet))}
                result.append(mapped[text[j]])
    return print(''.join(result))


# testing
vigenere(text='thisisatest', key='test', type='e')
vigenere(text='mlalbwsmxwl', key='test', type='d')
