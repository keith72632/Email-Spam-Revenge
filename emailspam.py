import smtplib, ssl
from time import sleep

def get_emails():
    with open('email.txt') as f:
        emails = f.readlines()
        sender = emails[0]
        receiver = emails[1]
        print(f'Sender Email address: {sender}')
        print(f'Reciever Email address: {receiver}')
        f.close()
        return sender, receiver

def send_email(senderaddr, receiveraddr):
    count = 1
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = senderaddr
    receiver_email = receiveraddr
    password = input("Type your password and press enter: ")
    message = """\
    \nSubject: Fuck you


    8===============================D---- $(Your Face)"""

    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        print('Connection Secure')
    except Exception as e:
        # Print any error messages to stdout
        print(e)

    try:
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        print('Login successful')
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    try:
        while(True):
            if count % 50 == 0:
                sleep(10)
                print('waiting...')
                count += 1
            else:
                server.sendmail(sender_email, receiver_email, message)
                print(f'Email #{count} sent to {receiver_email} successfully')
                count += 1
    except Exception as e:
        # Print any error messages to stdout
        print(e)

    finally:
        server.quit() 

if __name__ == '__main__':
    sender, receiver = get_emails()
    send_email(senderaddr=sender, receiveraddr=receiver)