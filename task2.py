def spin_words(sentence):
    new = sentence.split(" ")
    txt = ''
    for x in new:
        if len(x) > 4:
            txt += x[::-1] + ' '
        else:
            txt += x + ' '
    return txt

print(spin_words("hello man lolka"))