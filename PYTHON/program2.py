#2.Check if a String is a palindrome.#
x=int(input("enter a number: "))
num=x
rev=0
while num!=0:
    d=num%10
    rev=rev*10+d
    num=num//10
if x==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#input=121
#output=palindrome#
