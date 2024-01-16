t = int(input())

while t > 0:
    s = input()
    # Your code goes here
    t -= 1
    hlist = []
    newstr = ""
    n = len(s)
    ''' for i in range(len(s)-1):
        if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u') and (s[i+1] == 'a' or s[i+1] == 'e' or s[i+1] == 'i' or s[i+1] == 'o' or s[i+1] == 'u') and (s[i+2] == 'a' or s[i+2] == 'e' or s[i+2] == 'i' or s[i+2] == 'o' or s[i+2] == 'u'):
            newstr = newstr+s[i]+s[i+1]+s[i+2]
            #hlist.append(newstr)
    print(newstr)'''
    '''for i in range(len(s)-1):
        if s[i] == ('a','e','i','o','u') and s[i+1] == ('a','e','i','o','u') and s[i+2] == ('a','e','i','o','u'):
            newstr = newstr+s[i]+s[i+1]+s[i+2]
            #hlist.append(newstr)
        print(newstr)'''
    for i in range(len(s)-1):
        if i< n and i+1 < n and i+2 <n:
            if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u') and (s[i+1] == 'a' or s[i+1] == 'e' or s[i+1] == 'i' or s[i+1] == 'o' or s[i+1] == 'u') and (s[i+2] == 'a' or s[i+2] == 'e' or s[i+2] == 'i' or s[i+2] == 'o' or s[i+2] == 'u'):
                newstr = newstr+s[i]+s[i+1]+s[i+2]
                #hlist.append(newstr)
    print(newstr)

'''
t = int(input())

while t > 0:
    s = input()
    # Your code goes here
    t -= 1
    hlist = []
    newstr = ""
    n = len(s)
    for i in range(len(s)-1):
        if i< n and i+1 < n and i+2 <n:
            if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u') and (s[i+1] == 'a' or s[i+1] == 'e' or s[i+1] == 'i' or s[i+1] == 'o' or s[i+1] == 'u') and (s[i+2] == 'a' or s[i+2] == 'e' or s[i+2] == 'i' or s[i+2] == 'o' or s[i+2] == 'u'):
                newstr = newstr+s[i]+s[i+1]+s[i+2]
                #hlist.append(newstr)
    if len(newstr)>2:
        print("Happy")
    else:
        print("Sad") 
    '''