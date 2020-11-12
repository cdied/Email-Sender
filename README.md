# -----------------  Email sender  ---------------- #
author: Sayed Mohammad Rezaie -- 11.Nov.2020
github: @cdied



description:
1. Email sender application with GUI (tkinter)
2. App is using SMTP protocol to send email
3. to send email using gmail, hotmail or ..., code must be modifyed. you can find it inside the function section
4. imports tkinter, smtplib, email

-----------------------------------------------------

* following function is a Secure SMTP email sender for gmail.com
* smtp.gmail.com can be replaced with other email service providers
* in this case user have to login to his/her email by passing email and password
* port numbers 25, 587, 465, or 2525 can be used for SMTP_SSL
------------------------------------------------------
* email = "" >>> you need to your email address here >>> it should be matched with msg["From"]
* password = "" >>> you need to pass email's password here
------------------------------------------------------ 
     with smtplib.SMTP_SSL(smtp.gmail.com, 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(msg)
    
