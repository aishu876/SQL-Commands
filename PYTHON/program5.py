#5.Count the frequency of each Character in a string.
s=input("enter a string: ")
n={}
for i in s:
    if i in n:
        n[i]+=1
    else:
        n[i]=1
print(n)

#input:hello
#output:enter a string: hello
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
