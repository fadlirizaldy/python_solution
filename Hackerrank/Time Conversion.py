def timeConversion(s):
    if s[-2:].upper() == 'AM':
        p = s[:len(s)-2]
        if s[:2] == '12':
            p = p.replace(s[:2], '00')
        return p
    elif s[-2:].upper() == 'PM':
        a = str(int(s[:2])+(s[:2]!='12')*12)
        if len(a) == 1:
            a = "0" + a
        return s[:len(s)-2].replace(s[:2], a)