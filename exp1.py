a=56
b=8.7
c=True
d="pyhon"
e=(10,20,30,40)
f=[30,4,2,3,4]
g={0,9,8,7,6,5}
h={"A GRADE":90,"B GRADE":80}

print("Type of a:",type(a))
print("Type of b:",type(b))
print("Type of c:",type(c))
print("Type of d:",type(d))
print("Type of e:",type(e))
print("Type of f:",type(f))
print("Type of g:",type(g))
print("Type of h:",type(h))
i=0
while i<10:
    print("Square of",i,":",i**2)
    i=i+1
fact=1

for i in range(1,11):
    fact=fact*i
    print("Factorial of ",i,":",fact)

x=int(input("Enter a number:"))

if x>0:
    print("Number is positive")
elif x==0:
    print("Number is neither positive nor negative")
elif x<0:
    print("Number is negative")