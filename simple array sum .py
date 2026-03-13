def timeConversion(s):
    period = s[-2:]  # AM or PM
    time = s[:-2]    # strip AM/PM
    h, m, sec = time.split(':')
    h = int(h)
    
    if period == 'AM':
        if h == 12:
            h = 0  # 12:xx:xxAM → 00:xx:xx
    else:  # PM
        if h != 12:
            h += 12  # add 12 for PM hours except 12PM

    return f"{h:02d}:{m}:{sec}"

s = input()
print(timeConversion(s))
