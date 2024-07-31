text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

words = text.split()
new_text = []

for word in words:
    if word[-1] in ',.':
        sign = word[-1]
        word = word[:-1] + 'ing' + sign
    else:
        word += 'ing'
    new_text.append(word)

print(' '.join(new_text))
