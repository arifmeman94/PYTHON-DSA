# to print integers just add those numbers inside print statement
print(20)

#Adding 2 number
a=5
b=6
print(a+b)

#you can directly print result withought using variables
print(5+6)

#printing multiple values in same line, just add coma
print(7,"Hello")

#What will be the output of this code?
print(82, 2, " ", 3)

#What will be the output of this code? there is extra space after get
print("Add", 2, "and", 3, "to get ", 5)

#What is the difference between
print(12)
print(11)
#and

print(12)

print(11)

#Task
#Write a program which does the following
#Declare two variables x and y
#Assign the value True to x and the value False to y
#Output x and y space separated on a single line
x = True
y = False
print(x,y)

#Strings
#Concatenation
#The '+' sign can be used between strings to add them together to make a new string.
#This is called concatenation.
x = "Good"
y = "Work"
print(x + y)
print(x+ " " +y) # this will add space in between two words

#Python uses the + sign for both addition and concatenation.

#Numbers are added.
#Strings are concatenated.
#We cannot mix the two
#You are given a program which does the following

#You want to output 2569
#Try running the given code given in the IDE as it is - it will give a Compilation error
#Fix the error so that both the variables become strings and the output is 2569

# We need to output 2569 using string concatenation.
# The code below is incorrect - Debug the code to solve the problem

string1 = "25"
string2 = "69"

print(string1 + string2)

#string length
#We can use the len() function to get the length of a string.
#Task
#Write a program which does the following

#Create a variable txt and assign it the text NumeroTres
#Use the len() function to output to the console the number of characters in txt

txt = "NumeroTres"
print(len(txt))

#Outputting Characters from a String
#So the first character of a string s is s[0] , the second is s[1] , and so on.
#Task
#Write a program which does the following

#Create a string variable word and assign the text Programming to it
#Print the characters o and r from the string word in separate lines using the syntax defined above

word = "Programming"
print(word[2])
print(word[4])

#Task
#Write a program which does the following

#Initialize a string variable word and assign the value Ocygen to it.
#You now want to fix the typo in the given string.
#Use the syntax explained above to replace 'c' with 'x' in a new variable word_new
#Output the updated word_new to console

word = "Ocygen"
newstr = word.replace("c","x")
print(newstr)

#String slicing
#Task
#Declare a string variable var
#Assign the value String to it
#Use string slicing to print ring to the console.

var = "String"
print(var[2:6])

#Converting string to list using split method
#Task: returing length of last word in string
s= " Hello World " # here at the beginning and end blank spaces are there
newstr = s.strip()   # strip will remove starting and ending blank spaces
newlst = list(newstr.split(" "))  # split will split the string where blank spaces are there and list will convert it in to list
n = len(newlst) #length of new list we created
p = len(newlst[n-1]) # length of last word in list
print(p)

#checking String is palindrom or not
s = "2025"
newlist = list(s)
print(newlist)
newlist2= []
n = len(s)
i = 1
for j in range(len(s)):
    newlist2.append(s[n-i])
    i = i+1
print(newlist2)
if newlist == newlist2:
    print("Yes")
else:
    print("False")  

### function ex.
print("-------------------------")
n=6
sum = 0
i = 1
for i in range(n+1):
    if i%2 == 0:
        sum = sum+i
print(sum)

##### function ex, POW
print("-------------------------------------")
x = 2
n = 3
for i in range(n):
    x = x**n
print(x)
