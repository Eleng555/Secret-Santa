import random
import sendgrid
sg = sendgrid.SendGridClient(API_KEY_HERE)

### List of people participating ###
names = ['person1', 'person2', 'person3', 'person4', 'person5', 'person6',
         'person7', 'person8', 'person9', 'person10', 'person11', 'person12']


### Add names and emails of people participating ###
### Names must exactly match the ones in "names" array above ###
info = [('person1','santa1@mailinator.com'), ('person2','santa2@mailinator.com'),
          ('person3','santa3@mailinator.com'), ('person4','santa4@mailinator.com'),
          ('person5','santa5@mailinator.com'), ('person6','santa6@mailinator.com'),
          ('person7','santa7@mailinator.com'), ('person8','santa8@mailinator.com'),
          ('person9','santa9@mailinator.com'), ('person10','santa10@mailinator.com'),
          ('person11','santa11@mailinator.com'), ('person12','santa12@mailinator.com')]


### Assigns who gets who and makes sure you don't get yourself ###
a = False
ctr = 1
while ctr > 0:
    random.shuffle(names)
    for x in range (0, len(names)):
        if names[x] == info[x][0]:
            a = True
    if a == True: #if a person gets themself, reshuffle
        ctr = 1
        a = False
    else:
        ctr = -1 #exits while loop


### Emails people one by one ###
for x in range(len(names)):
    message = sendgrid.Mail()
    message.add_to(info[x][1]) #add recipient
    message.set_subject("Secret Santa 2015")
    message.set_html("""<link href='https://fonts.googleapis.com/css?family=Karla:400,700' rel='stylesheet' type='text/css'>
    <div style="font-family:Karla,sans-serif;"> <h1>hi there</h1>
    <p>for this year&#39;s secret santa, your person is: """ + names[x] + """</p></div>""") #set email message
    message.set_from("SENDER NAME <SENDER_EMAIL@example.com>") #sender info
    status = sg.send(message)
