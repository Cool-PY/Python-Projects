Alphabets = 'abcdefghijklmnopqrstuvwxyz'
reversedAlphates = 'zyxwvutsrqponmlkjihgfedcba'

Alphabets = list(Alphabets)
reversedAlphates = list(reversedAlphates)

while 1:
    msg = input('Your Message\n: ')
    msg = msg.lower()

    if msg=='$q' or msg=='$quit':
        break

    secretMessage = ''

    for l in msg:
        for al in Alphabets:
            if l == al:
                index = Alphabets.index(al)
                secretMessage += reversedAlphates[index]

        if l == ' ':
            secretMessage += ' '

    print(f'\nYour Message is\n{secretMessage}\n')


