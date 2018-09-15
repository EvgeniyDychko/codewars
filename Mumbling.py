def accum(s):
    new = list(s)
    i = 0
    txt = ''
    while i < len(new):
        if i == 0:
            txt += new[i].upper()
        elif i == len(new) - 1:
            txt = txt + '-' 
        else:
            txt = txt + '-' + new[i].upper() + i * new[i]
        i += 1
    return txt