import re
ss=[]
n=int(input('Enter strings number: '))
for i in range(n):
 str=input()
 str=re.sub(r'(^%%)', r'', str)
 if str.startswith('##'):
  continue
 ss.append(str)
print(*ss, sep='\n')
