def capitalize(string):
    ret = ""
    strings = []
    strings = string.split(" ")
    for i in range(0, len(strings) - 1):
        ret += strings[i][0].upper() + strings[i][1:].lower() + " "
    ret +=  strings[-1][0].upper() + strings[-1][1:].lower()



    return ret
