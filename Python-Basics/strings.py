#strings in python are arrays
a = "Hello"
print(a[0]) # prints first character of string
print("--------------------------------------------------------------------")
#looping through strings
a = "Hello"
for i in a:
    print(i) # prints first to last character of strings
print("--------------------------------------------------------------------")
#length of string is know from len() method
a ="Hello"
length = len(a) # checks length of stings and retuns 5
print(length)
print("--------------------------------------------------------------------")
#check strings: to check perticular word/phrase in stinrg we can use in
a = "Hello World, my first programm"
if "my" in a:
    print("my")
print("--------------------------------------------------------------------")
#smilarly NOT in can be used to check word/phrase not in string
txt = "The best things in life are free!"
print('add' not in txt)
print("--------------------------------------------------------------------")
#in if condition 
if "add" not in txt:
    print("it is not")
print("--------------------------------------------------------------------")
#slicing through string 
#you can use [start index:end index] to slice
print("index 2 to 4, 5 is not returned:",txt[2:5]) # it will print characters from index 2 to index 4, last index is not returned (Ex: e, black space, b)
print("index 0 to 4, 5 is not returned:",txt[:5])  #this will slice from 0 to 4th index
print("from index to till end:", txt[2:]) # slice from 2 to end of string
print("--------------------------------------------------------------------")
#negative indexing
#negative is used to slice from end of the string
#negative index starts from -1
str = "World"
str2 = str[::-1]
str3 = str[-1:-5:-1] # [start:stop:step]
print(str, str2, str3)
print("--------------------------------------------------------------------")
#modification of string
#upper case
txt = "hello world"
news = txt.upper() #converts full string in upper case
print(news)
print(news.lower()) #returns string in lower case
print("--------------------------------------------------------------------")
#remove white space
txt1 = " Hello World "
print(txt1) #with blank space
print(txt1.strip()) # withought blank space
print("--------------------------------------------------------------------")
