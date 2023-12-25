strs=[]
n=''
while n!= 'стоп':
 n=input()
 strs.append(n)
shortest=min(strs, key=len)
longest=max(strs, key=len)
if set(longest)>=set(shortest):
 print('ДА')
else:
 print('НЕТ')
