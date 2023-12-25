strs=[]
try:
 n=int(input('Введите кол-во строк: '))
 for i in range(n):
  strs.append(input().lower())
 if any('кот' in s for s in strs):
  print ('МЯУ')
except ValueError:
 print ('Неверное число строк')
