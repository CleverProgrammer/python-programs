import urllib

def read_text():
    quotes = open("/Users/Rafeh/Dropbox/Calculus One/movie_quotes.txt")
    contents = quotes.read()
    print (contents)
    check_profanity(contents)
    quotes.close()
    


def check_profanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
    output = connection.read()
    print (output)
    if "true" in output:
        print ("Profanity Alert!!")
    elif "false" in output:
        print ("No Profanity Detected")
    else:
        print ("Could not scan the document properly")
    connection.close()

read_text()
#check_profanity(contents)
    
