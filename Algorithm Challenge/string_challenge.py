
string1 = "abcde"
string2 = "abcdef"
empty = []

def f(string1, string2):
    if string1 == string2:
        print ('Each of the strings contain the same characters.')
    elif string1 != string2:
        for x in string2:
            if x not in string1:
                return x

print (f(string1, string2))
