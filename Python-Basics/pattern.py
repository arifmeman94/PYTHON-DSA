'''
for i in range(0,6):
    for j in range(0,6):
        print(f"{i}{j}", end=" ")
    print(" ")
    '''

''' 
for i in range(0,6):
    for j in range(0,i+1):
        print(j+1, end=" ")
    print("")

    '''
t = int(input())

while t > 0:
    n = int(input())
    s = input()
    r = input()
    # Your code goes here
    t -= 1
    if s == (s+11):
        print("1")