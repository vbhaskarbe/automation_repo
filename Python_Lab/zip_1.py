# Function to change string to a new character
 
def newString(charSet,input):
 
    # map original character set of english
    # onto new character set given
    origCharSet = 'abcdefghijklmnopqrstuvwxyz'
    mapChars = dict(zip(charSet,origCharSet))
 
    # iterate through original string and get
    #  characters of original character set
    changeChars = [mapChars[chr] for chr in input] 
 
    # join characters without space to get new string
    print (''.join(changeChars))
 
# Driver program
if __name__ == "__main__":
    charSet = 'qwertyuiopasdfghjklzxcvbnm'
    input = 'utta'
    newString(charSet,input)



