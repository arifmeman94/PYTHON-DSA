t = int(input())

while t > 0:
    n = int(input())
    s = input()
    # Your code goes here
    t -= 1
    str2list = []
    for i in range(0,len(s),2):
        str2lists = s[i:i+2]
        str2list.append(str2lists)
    print(str2list)

    for i in range(0,len(str2list),1):
        if str2list[i] == '00':
            str2list[i] = "A"
        elif str2list[i] == '01':
            str2list[i] = 'T'
        elif str2list[i] == '10':
            str2list[i] = 'C'
        elif str2list[i] == '11':
            str2list[i] = 'G'
    final = ""
    final = final.join(str2list)
    #print(str2list)
    print(final)