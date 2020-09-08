
# Get the cipher offset from user
offset = False
for _ in range(3):
    try:
        offset = int(input('Ange antal skiftningar >> '))
        offset
        break
    except ValueError:
        continue

assert offset


# Get the text to be ciphered from user
text = False
for _ in range(3):
    try:
        text = input('Ange text >> ')
        assert len(text) > 3
        break
    except (ValueError, AssertionError):
        continue

assert text


# Construct cipher
al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
      'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
      'S', 'T', 'U', 'V', 'W', 'X', 'Y',  'Z', 'Å',
      'Ä', 'Ö']
au = [a.lower() for a in al]
ciphered_text = ''

for index, symbol in enumerate(text):
    if symbol not in au and symbol not in al:
        ciphered_text += symbol
    elif symbol in al:
        ciphered_text += al[(al.index(symbol)+offset) % (len(al)-1)]
    elif symbol in au:
        ciphered_text += au[(au.index(symbol)+offset) % (len(au)-1)]

print(ciphered_text)
