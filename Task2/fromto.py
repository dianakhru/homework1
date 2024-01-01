numbers=[]
n=int(input('How many numbers?'))
for i in range(n):
 numbers.append(int(input()))
firstn=int(input())-1
lastn=int(input())-1
newlst=[]
for n, i in enumerate(numbers):
 if n >= firstn and n <= lastn:
  newlst.append(i)
print (sum(newlst))
