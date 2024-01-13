#Let us revisit our favourite rectangle and its area problem

#Write a program which does the following

#Declare 2 integer variables length and width
#In this problem - accept 2 user defined inputs from the console and initialize these values length and width
#Create another integer variable area - compute the area of the rectangle and store it as area
#Output area to the console

length = int(input())
width = int(input())
area = length*width
print("Area of the rectangle is:",area) # can not concate str and int, so used "," it will print Area of the rectangle is: area