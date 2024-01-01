import re
passwd=input('Введите пароль: ')
passwd2= input('Подтвердите пароль: ')
if passwd2 != passwd:
 exit('Пароли не совпадают!')
def password_level(pwd):
 res='Undefined'
 d_only="^[0-9]+$"
 up_only="^[A-Z]+$"
 low_only="^[a-z]+$"
    
 if len(pwd) < 8:
  res='Недопустимый пароль'
 if (len(pwd)>=8 and pwd.isnumeric() or 
    re.match(r"^[a-z]+$", pwd) or
    re.match(r"^[A-Z]+$", pwd)):
     res='Ненадежный пароль'
 if all(c.isdigit() or c.islower() for c in pwd) and \
       any(c.isdigit() for c in pwd) and \
       any(c.islower() for c in pwd):
  res='Слабый пароль'
 if all(c.isupper() or c.islower() for c in pwd) and \
       any(c.isupper() for c in pwd) and \
       any(c.islower() for c in pwd):
  res='Слабый пароль'
 if all(c.isupper() or c.isdigit() for c in pwd) and \
       any(c.isupper() for c in pwd) and \
       any(c.isdigit() for c in pwd):
  res='Слабый пароль'
 if (len(pwd) >= 8 and
    re.search(r'\d+', pwd) and 
    re.search(r'[a-z]+', pwd) and
    re.search(r'[A-Z]+', pwd) and
    re.search(r'\W+', pwd) and not
    re.search(r'\s+', pwd)):
     res='Надежный пароль'
 return print(res)

password_level(passwd)
