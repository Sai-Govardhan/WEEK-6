#24331A05I6

name=input("Enter any string : ")
print("Your string : ",name)
reverse=name[::-1]
print("Your Reverse string : ",reverse)
if(name==reverse):
    print("Given string is palindrome")
else :
    print("Given string is not palindrome")