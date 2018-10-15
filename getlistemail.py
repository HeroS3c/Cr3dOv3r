import json
import sys,os
emailn= input('how many email u have? ')
emaillist= []
for i in range(emailn):
 	email = emaillist.append(raw_input('email: '))
    

filename= 'email.json'


with open(filename, 'w') as f_obj:
    json.dump(emaillist, f_obj)
