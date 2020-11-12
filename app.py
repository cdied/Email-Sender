# -----------------  Email sender  ---------------- #
# author: Sayed Mohammad Rezaie -- 11.Nov.2020
# github: @cdied --- email: cdiedwbh@gmail.com

# description:
# 1. Email sender application with GUI (tkinter)
# 2. App is using SMTP protocol to send email
# 3. to send email using gmail, hotmail or ..., code must be modifyed. you can find it inside the function section
# 4. imports tkinter, smtplib, email

# -------------------  imports  ------------------- #
from tkinter import *
import smtplib
from email.message import EmailMessage


# ------------------  Functions  ------------------ #

# sending email with unencrypted SMTP
# given port number (1025) for test
# in this case, port number must be modifyed by user
# 
# *********! receiver must be "localhost" !******** #
#
def send_email():
    msg = EmailMessage()
    msg["Subject"] = subject.get()
    msg["From"] = sender.get()
    msg["To"] = receiver.get()
    msg.set_content(t_text.get("1.0", "end-1c"))

    try:
        with smtplib.SMTP(msg["To"], 1025) as smtp: #port must be modifyed by user
            smtp.send_message(msg)
            Label(root, text="Email sent successfully", background="#1A3D56", foreground="green", font=("Calibri", 16)).place(relx=0.6, rely=0.9, width=300, height=30)
    except:
        Label(root, text="Somthing went wrong", background="#1A3D56", foreground="red", font=("Calibri", 16)).place(relx=0.6, rely=0.9, width=300, height=30)


    # following comment are a Secure SMTP email sender for gmail.com
    # gmail.com can be replaced with other email service providers
    # in this case user have to login to his/her email by passing email and password
    # port numbers 25, 587, 465, or 2525 can be used for SMTP_SSL

    # email = "" >>> you need to modify email address here >>> it should be matched with msg["From"]
    # password = "" >>> you need to modify email's password here
    #
    # with smtplib.SMTP_SSL(smtp.gmail.com, 465) as smtp:
    #    smtp.login(email, password)
    #    smtp.send_message(msg)
    #


# ---------  GUI(Graphic user interface)  --------- #
root = Tk()
root.title("Email Sender")

sender = StringVar()
receiver = StringVar()
subject = StringVar()

canvas = Canvas(root, width=1000, height=700, background="#1A3D56").pack()

w_lable = Label(root, text="Welcome to Email Sender", background="#1A3D56", foreground="white")
w_lable.place(relx=0.5, rely=0.05, anchor=CENTER)

s_lable = Label(root, text="Your Email:", background="#1A3D56", foreground="white")
s_lable.place(relx=0.1, rely=0.1, width=100, height=30)

s_entry = Entry(root, textvariable=sender)
s_entry.place(relx=0.3, rely=0.1, width=600, height=30)

r_lable = Label(root, text="Reciver Email:", background="#1A3D56", foreground="white")
r_lable.place(relx=0.1, rely=0.17, width=100, height=30)

r_entry = Entry(root, textvariable=receiver)
r_entry.place(relx=0.3, rely=0.17, width=600, height=30)

sub_lable = Label(root, text="Email Subject:", background="#1A3D56", foreground="white")
sub_lable.place(relx=0.11, rely=0.3, width=80, height=30)

sub_entry = Entry(root, textvariable=subject)
sub_entry.place(relx=0.11, rely=0.35, width=790, height=30)

t_lable = Label(root, text="Text:", background="#1A3D56", foreground="white")
t_lable.place(relx=0.1, rely=0.4, width=60, height=30)

t_text = Text(root)
t_text.place(relx=0.11, rely=0.45, width=790, height=300)

s_button = Button(root, text="SEND EMAIL", command=lambda:send_email())
s_button.place(relx=0.11, rely=0.9, width=200, height=30)


root.mainloop()