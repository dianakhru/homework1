buys=[]
try:
 n=int(input('Введите кол-во покупок: '))
 for i in range(n):
  buys.append(input())
 for i in buys:
  print (i)
except ValueError:
 print ('Incorrect purchase number')
