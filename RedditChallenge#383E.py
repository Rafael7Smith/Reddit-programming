#https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/
def movechars(strvar):
    firstchar = strvar[0]
    for i in range(len(strvar)):
        if(i == len(strvar)-1):
            strvar[i] = firstchar
            break
        else:
            strvar[i] = strvar[i+1]
   
    return strvar
    
    
def same_necklace(string1, string2):
    message = string1 + " " + string2
    string1 = list(string1)
    string2 = list(string2)
    flag = False;
    if(string1 == string2):
        message += " True"
    else:
        for i in string1:
            string1 = movechars(string1)
            if(string2 == string1):
                message += " True"
                flag = True
                break;
        if not flag:
            message += " false"
    
    print(message)
    return

same_necklace("nicole", "icolen")
same_necklace("nicole", "lenico")
same_necklace("nicole", "coneli")
same_necklace("aabaaaaabaab", "aabaabaabaaa")
same_necklace("abc", "cba")
same_necklace("xxyyy", "xxxyy")
same_necklace("xyxxz", "xxyxz")
same_necklace("x", "x")
same_necklace("x", "xx")
same_necklace("x", "")
same_necklace("", "")
