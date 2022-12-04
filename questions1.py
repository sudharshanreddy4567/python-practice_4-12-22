#program to multiply all the elements in a list
n=int(input("Enter the number of elements you want in list: "))
l=[]
for i in range(n):
    el=int(input("Enter element: "))
    l.append(el)

mul=1
for c in l:
    mul=mul*c
print(mul)