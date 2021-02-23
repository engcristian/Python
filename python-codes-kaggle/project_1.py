'''
How to send many emails using python and showing in details the diferents elements from dataframe.
Sendiang an email to directorship diferently from stores, in total 26 emails sent.
'''

import pandas as pd
import smtplib
import email.message
#here you'll type your password, to keep this program more safety.
email_password = input('Type your password: ')
#using a function to send email automaticaly by Python
def send_email(store_resume, store):
    server = smtplib.SMTP('smtp.gmail.com:587')  
     #put here the message for the e-mail body
    corpo_email = f'''
    <p>This e-mail is a test for this project, below you can see
    a dataframe from the main Shoppings in Brazil</p>
    {store_resume.to_html()}
    <p> Thank yoou</p>      
    '''

    msg = email.message.Message()
    msg['Subject'] = "Email subject" #Change the e-mail's subject here
    
    
    msg['From'] = 'your_email@gmail.com' #insert the e-mail that will send
    msg['To'] = 'receiver@anyemail.com' # the email that will receive
    #here your password is hidden, so only when the program is running that you'll insert your email
    password = email_password 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email sent')
#Reading the xlsx dataframe
df = pd.read_excel('Vendas.xlsx')
#Getting the billing from the dataframe ID Loja and Valor Final
billing = df[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
#Sorting the elements from billing by False ascending
billing = billing.sort_values(by='Valor Final', ascending=False)
#Doing the same to get the amount from each Shopping by ID Loja and Quantidade
amount = df[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#Also sorting the elements from amount by False ascending
amount = amount.sort_values(by='ID Loja', ascending=False)
#calculating the average tickt from each shopping
average_ticket = (billing['Valor Final']/amount['Quantidade']).to_frame()
#Renaming the column 0 to Average Ticket
average_ticket = average_ticket.rename(columns={0:'Average Ticket'})
#Sorting the elements from average ticket by false ascending
average_ticket = average_ticket.sort_values(by='Average Ticket', ascending=False)
#Selecting only the stores' name from each shopping
stores= df['ID Loja'].unique()
#email for the directorship with more informations
director_resume = billing.join(amount).join(average_ticket)
send_email(director_resume, 'All stores')
#Using FOR to create a repetition beteween 25 shoppings while sending emails
for store in stores:
    store_index = df.loc[df['ID Loja'] == store, ['ID Loja','Valor Final','Quantidade']]
    store_resume = store_index.groupby('ID Loja').sum()
    store_resume['Average Ticket']  = store_resume['Valor Final'] / store_resume['Quantidade']
    send_email(store_resume, stores)
