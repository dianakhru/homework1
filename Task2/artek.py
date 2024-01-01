def Artek(students, fn):
 data=dict(substr.split(" ") for substr in students.split(', '))
 data= { k:v for k, v in data.items() if v=='5' }
 data= dict(sorted(data.items())[:fn])
 return print (*data.keys(), sep=', ')

students_list=input('Введите список учеников с оценками: ')
free_places=int(input('Введите кол-во свободных мест: '))
Artek(students_list, free_places)
