#24331A05I6

name=input("Enter any string : ")
c=0
for i in range(len(name)):
    if(name[i]=='a'):
        s=name.replace('a','x')
        c+=1
if c==0:
    print("There is no a letter in given string")
else :
    print(s)
