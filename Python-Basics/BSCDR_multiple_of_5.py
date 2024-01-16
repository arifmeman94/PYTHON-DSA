''' 
n = 15
out = []
for i in range(1,n+1):
    if i%5 == 0:
        out.append(i)
print(out) '''

'''
class MultipleOfFive:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
         n = self.n
         out = []
         for i in range(1,n+1):
              if i%5 == 0:
                   out.append(i)
         return out
         '''
'''
n = 2
m = 10
for i in range(1,m+1):
    print(n*i)
    '''
S = input()
N = int(input())

for i in range(N):
    W = input()
    for j in range(len(W)-1):
        if W[j] in S:
            print("yes")
        else:
            print("No")