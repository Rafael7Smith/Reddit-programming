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
    morsedictionary = dict(zip(string.ascii_lowercase, alphabetraw.split()))
    print morsedictionary
    #splitmessage = textwrap.wrap(input, 3)
    #splitmessage = list(map(''.join, zip(*[iter(input)]*2)))
    splitmessage = tuple(input[i:i+3] for i in range(0, len(input),3))
    print(splitmessage)
    for char in splitmessage:
        print char
        if char in morsedictionary:
             print morsedictionary[char]
    
    print(morsedecoded)
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