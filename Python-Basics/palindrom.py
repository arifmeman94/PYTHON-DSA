''' class Palindrome:
    def __init__(self, n):
        self.n = "2002"
        
    def check(self):
        newlist = list(self.n)
        #print(newlist)
        newlist2= []
        n = len(self.n)
        i = 1
        for j in range(len(self.n)):
            newlist2.append(self.n[n-i])
            i = i+1
        #print(newlist2)
        if newlist == newlist2:
            s = "true"
        else:
            s = "flase"
        print(s) 
        '''
''' class Palindrome:
    def __init__(self, n):
        self.n = n
        
    def check(self):
        #s = self.n
        self.n = "2002"
        s = self.n
        list1 = list(s)
        n = len(s)
        i = 1
        list2 = []
        for j in range(n):
            list2.append(s[n-i])
            i = i+1
        return list2 '''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''y = str(x)
        list1 = list(y)
        n = len(y)
        i = 1
        list2 = []
        for j in range(n):
            list2.append(y[n-i])
            i = i+1
        if list1 == list2:
            return True
        else:
            return False '''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        ''' list1 = list(y)
        n = len(y)
        i = 1
        list2 = []
        for j in range(n):
            list2.append(y[n-i])
            i = i+1 '''
        if y == y[::-1]:
            return True
        else:
            return False