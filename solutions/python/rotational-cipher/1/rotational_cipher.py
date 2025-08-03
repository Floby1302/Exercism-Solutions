def rotate(text, key):
    s=''
    temp1='abcdefghijklmnopqrstuvwxyz'
    temp2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in text:
        if i in temp1:
            idx = temp1.index(i)
            s += temp1[(idx + key) % 26]
        elif i in temp2:
            idx = temp2.index(i)
            s += temp2[(idx + key) % 26]
        else:
            s += i
    return s