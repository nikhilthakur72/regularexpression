#question 1
import re
a=('the email is nikhilthakur031@gmail.com test')
b=list(a.split(' '))
for i in b:
    match=re.finditer('^[\w]*(@)(gmail.com|yahoo.com)',i)
    for i in match:
        print(i.group())


#question 2
import re
a=('9779039831')
b=list(a.split(' '))

for i in b:
    match=re.finditer('^[6-9][0-9]{9}',i)
    for i in match:
        print(i.group())
