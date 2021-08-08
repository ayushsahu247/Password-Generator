import numpy as np
import random

import smtplib
from email.message import EmailMessage

import sys



#Dependencies: Install Numpy.

#edits to make the code work
#insert your emailID and password in place of the placeholders
'''
open your gmail
> Click on your profile picture
> Goto Manage Your Google Account
> Go to Security
> Disable 'Use your phone to sign in'
> Disable 'Two Step Verification'
> Turn on Less Secure App Access
> This should work.
This method is slightly less secure. If you don't care, go ahead.
But if you are paranoid, watch this video by Corey Schafer to learn
to do this in a more secure manner.
https://www.youtube.com/watch?v=JRCJ6RtE3xU

I suggest that you make a new google account for this, so as to
keep you main account clean and have a separate place for all your
credentials.

'''
#Execute this command on your terminal
#python3 passwordGenerator.py <website> <userID>


def select(list, n):   
	#randomly selects n elements from given list
    arr=[]
    for i in range(n):
        arr.append(random.choice(list))
    return arr

def constSumList(Sum, n):
    # returns a list of n positive integers with given Sum
    counter = list(np.repeat(1,n))
    while (sum(counter)!=Sum):
        counter[random.choice(np.arange(n))]+=1
    return counter
constSumList(10,4)

def passwordGenerator(n=10):
    lowercase = list(map(chr, range(ord('a'), ord('z'))))
    uppercase = list(map(chr, range(ord('A'), ord('Z'))))
    numbers = list(np.arange(0,10).astype(str))
    symbols=['#', '@', '$', '&', '*']

    domain = [lowercase, uppercase, numbers,symbols]

    counter = constSumList(n, 4)

    password = []
    for i in range(4):
        password += select(domain[i], counter[i])
    random.shuffle(password)
    password = "".join(password)
    return password

password = passwordGenerator()

msg = EmailMessage()
msg['Subject'] = sys.argv[1] + "Credentials"

#set both of these to your own
msg['From'] = 'from@gmail.com'  
msg['To'] = 'target@gmail.com'
msg.set_content('Your userID and password for {}:\n {} {}'.format(sys.argv[1], sys.argv[2], password ))
print('Your UserID and password for {}: {}\n {}'.format(sys.argv[1], sys.argv[2],password))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login('placeholder_email', 'placeholder_password')
    smtp.send_message(msg)
