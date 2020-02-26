# My Program for query... TEST
#
# Input --> for Name=input("Enter your Name:")
# Input --> for Age=input("Enter you Age:")
# Input --> for Email=input("Enter your e-mail:")
# Name: 
# Age:
# e-mail:
#
# Questions:
# Q1; Q2; Q3; Q4; Q5; Q6; Q7; Q8; Q9;
#
# Answers:
# choose one of the following options: 
# A) B) C)
#
# Mister/Miss $Name,
# Result: You have: "2 A)" and "3 B)" and "4 C)"
#  
# Thank you for your time. 
# We will also send you the results over e-mail to have it!
#
#
#


print("")
name=input("Enter your name: ")
age=input("Enter your age: ")
email=input("Enter your e-mail: ")
print("\a")


Questions=['Kolko pati hodish na fitnes: A) B) C)', 'Kolko pati qdesh na den: A) B) C)', 'Kolko chasa spish na denonoshtie: A) B) C)', 'Zasho: A) B) C)']
possible_answers = ['A','B','C']

Answers = []
score_a = 0
score_b = 0
score_c = 0
for q in Questions:
    a=input(q)
    while a not in possible_answers:
       a=input(q)
    Answers.append(a)
    if a == 'A':
        score_a += 1
    if a == 'B':
        score_b += 1
    if a == 'C':
       score_c += 1

print("")
print(name + " ,you have:")
print("A :" + str(score_a))
print("B :" + str(score_b))
print("C :" + str(score_c))
print("You have: ", Answers)
print("")
print("Thank you for your time. We will also send you the results over e-mail to have it.")
print("Soon we will receive a reply at " + email)
# print ( len(Answers) )
# print("\n")
# print("Your name is: " + name)
# print("Your age is: " + age)
# print("Your email is: " + email)



#
# output to a file
#

import os
import sys
if not os.path.exists("/home/mitaka/test/test1"):
    os.makedirs("/home/mitaka/test/test1")
with open ("my-program.txt", 'w') as f:
    f.write(str(name) + ", you have: " + str(Answers) + "\n")


##
## Trying to add email functionality to my code -- It works!
##
'''
import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "dimitar.pisarov@dreamix.eu"
receiver_email = "denis.danov@dreamix.eu"
password = input("Type your password and press enter:")
message = """\
Subject: Hi Denis

This is automatically message by my Python program."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
'''








