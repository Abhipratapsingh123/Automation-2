from urllib.parse import uses_netloc
import yagmail
import os
import time
import pandas as pd

sender = 'fee.mca@gmail.com'


subject = 'Sending to csv'

content = """
Hello Akshat, Sakshi this side.
Can you share your video which you uploaded for the Upgrad's internship.
My whatsapp is not working, that's why I am emailing you.
Please share if you can.
"""
yag = yagmail.SMTP(user= sender, password=os.getenv('PASSWORD'))
df = pd.read_csv('Segment-4/contacts.csv')

for i in df['email']:
  yag.send(to=i,subject=subject,contents=content)
  print("Email sent!")
  time.sleep(1)


