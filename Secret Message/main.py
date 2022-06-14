Alphabets = 'abcdefghijklmnopqrstuvwxyz'
reversedAlphabtes = 'zyxwvutsrqponmlkjihgfedcba'

Alphabets = list(Alphabets)
reversedAlphabtes = list(reversedAlphabtes)

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
                secretMessage += reversedAlphabtes[index]

        if l == ' ':
            secretMessage += ' '

    print(f'\nYour Message is\n{secretMessage}\n')


