def log(text):
    flog = open("logb.txt", "a")
    newLine = """\n"""""
    textPlusNewLine =  str(datetime.datetime.now().time()) + " :: " + text + newLine
    flog.write(textPlusNewLine)
    flog.close()

def exampleFunc(str):
    log("hello world")
    return str

#-- ESRI SPLITTER --#

exampleFunc(!NAME!)
