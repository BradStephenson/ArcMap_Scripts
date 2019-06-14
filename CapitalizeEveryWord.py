# @Author Bradley Stephenson

def capitalize(string):
    
    # setup a return string and a list of all the words in the given string
    ret = ""
    strings = []
    strings = string.split(" ")
    
    # start building the string by capitalizing the first character of each word 
    for i in range(0, len(strings) - 1):
        ret += strings[i][0].upper() + strings[i][1:].lower() + " "
    # Do the last word and don't add the " "
    ret +=  strings[-1][0].upper() + strings[-1][1:].lower()


    # Return the string that was built
    return ret
