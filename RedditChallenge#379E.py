#https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/
def tax(income):
    message = "tax(" + str(income) + ") =>"
    tax = 0
    taxbrackets = {0.4: 100000, 0.25: 30000, 0.1: 10000}
    bracketcap = [100000,30000,10000]
    bracketrate = [0.4,0.25,0.1]
    #print(taxbrackets)
    #print(list(taxbrackets.items()))
    for (i,r) in zip(bracketcap, bracketrate):
        #print("checking incomecap: " + str(i) + " and rate: " + str(r))
        if income > i:
            tax += (income - i) * r #550,400...... 450400 * 0.4, then tax the 100,000
            income = i
            #print("Amount: " + str(income - i) + " taxed at: " + str(r))
    print(message + str(int(tax)))
    return

tax(0)
tax(10000)
tax(10009)
tax(10010)
tax(12000)
tax(56789)
tax(1234567)
