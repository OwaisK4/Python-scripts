#!/usr/bin/python
import random

messages = ['It is certain','It is decidedly so','Yes definitely','Reply hazy try again', 'Ask again later','Concentrate and ask again','My reply is no','Outlook not so good','Very doubtful']

for i in range(len(messages)):
    print(messages[random.randint(0,len(messages) - 1)])

