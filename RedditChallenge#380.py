#https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/
import string
def smorse(message):
    morsecode = ""
    alphabetraw = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
    morsedictionary = dict(zip(string.ascii_lowercase, alphabetraw.split()))
    #print(morsedictionary)
    
    for char in message:
        morsecode += morsedictionary[char]
    print(morsecode)
    return

#https://www.reddit.com/r/dailyprogrammer/comments/cn6gz5/20190807_challenge_380_intermediate_smooshed/
import textwrap
def smalpha(input):
    morsedecoded = ""
    alphabetraw = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
    morsedictionary = dict(zip(alphabetraw.split(), string.ascii_lowercase))
    print morsedictionary
    #this will need to be redone - misunderstood the premise, each letter only appears once
    #this program attempts to decode via:
    #check 3 characters for a matching letter
        #if none
            #check first 2 char for matching letter
            #move position, repeat
        #else
            #move position, repeat
    position = 0
    while(position < len(input)-1):
        checkcode = ''
        char3flag = False
        #grab 2 characters
        for i in range(3):
            checkcode += input[(i+position)]
        if checkcode in morsedictionary:
            #print morsedictionary[checkcode]
            morsedecoded += morsedictionary[checkcode]
            char3flag = True
        if not char3flag:
            #grab 3 characters
            for i in range(2):
                checkcode += input[(i+position)]
            if checkcode in morsedictionary:
                #print morsedictionary[checkcode]
                morsedecoded += morsedictionary[checkcode]
            position += 2
        else:
            position += 3
    
    print(morsedecoded)
    print("Ended on position: " + str(position) + " message length: " + str(len(input)))
    return
    
    
smorse("sos")
smorse("daily")
smorse("programmer")
smorse("bits")
smorse("three")
smorse("w")

print("---------------")

smalpha(".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..")
#smalpha(".----...---.-....--.-........-----....--.-..-.-..--.--...--..-.---.--..-.-...--..-")
#smalpha("..-...-..-....--.---.---.---..-..--....-.....-..-.--.-.-.--.-..--.--..--.----..-..")

#smalpha(smorse("sos"))