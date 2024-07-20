import yagmail
import os
import time

sender = 'fee.mca@gmail.com'
receiver = 'abhi.2@sushantuniversity.edu.in'

subject = 'Upgrad video'

content = """
Hello Akshat, Sakshi this side.
Can you share your video which you uploaded for the Upgrad's internship.
My whatsapp is not working, that's why I am emailing you.
Please share if you can.
"""
yag = yagmail.SMTP(user = sender, password =os.getenv('PASSWORD'))

for _ in range(4):
  time.sleep(4)
  yag.send(to = receiver, subject = subject, contents = content)
  print("Email sent!")



