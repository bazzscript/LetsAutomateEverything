#Author : Bezaleel Nwabia 
#Department: Tech With Bazz

import sys
import smtplib
import pandas as pd
from email.message import EmailMessage

MailAddress = input(str("What's your mail adrress? : "))
MailPassword = input(str("What's your mail/app password? : "))

#enter it manually via cli
# RmailAddress = [item for item in input(str("The Reciever(s) mail adrress(es)? : ")).split(',')]

#or just give the script an excel mail list
pathtolist = input(str('Type in Path to Email Excel List: '))
e = pd.read_excel(pathtolist)
RmailAddress = e["Emails"].values

msg = EmailMessage()
msg['Subject'] = input('Email Subject/Purpose? : ')
msg['From'] = MailAddress
msg['To'] = ', '.join(RmailAddress)
msg.set_content(input('Type in your message / mail here : '))

#this block of code handles html mails
#msg.add_alternative("""\ add html code here""")#add html code, that is html email


#this block of code handles mail attachments
attach_prompt = input('Do you want to add an attachment? Type in YES or NO : ').upper()
if attach_prompt == 'YES':
    #asking nicely so as to give better instruction
    multiattachconfirm = input('Multiple Attachment (Enter YES)\nJust one attachment (Enter NO)\n :').upper()
    if multiattachconfirm == 'YES':
        print("PLEASE SEPERATE WITH or TYPE IN ',' AFTER EACH FILE PATH ENTERED")
    elif multiattachconfirm == 'NO':
        pass
    else:
        print("What the fuck did you type?\nCan't you read instructions\nAm sorry but fuck you, AM OUT!\n\nSCRIPT CRASHED BECUASE OF YOU! YOU!! YOU!!!!")
        sys.exit()
    
    #getting attachment file path from user, we can also get multiple attachment
    which_attachment = []   
    which_attachment = [item for item in input(str("Carefully Type in System Path To Attachment : ")).split(',')]
    for file in which_attachment:
        with open(file,'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
elif attach_prompt == 'NO':
    pass

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(MailAddress, MailPassword)
    smtp.send_message(msg)