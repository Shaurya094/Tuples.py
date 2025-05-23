x = (1,2,3,3,2,1)
def p(x):
    l = len(x) - 1
    s = 0
    while (s<l):
        if (x[s] != x[l]):
            return False
        s+=1
        l-=1
    return True

if p(x):
    print ("It's a palindrome")
else:
    print ("It's not a palindrome.")