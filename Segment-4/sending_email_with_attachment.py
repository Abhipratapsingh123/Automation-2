import yagmail
import os

sender= 'fee.mca@gmail.com'

receiver = 'vnapowoeg@emlhub.com'

subject = 'This is the subject'

content = """
Hello Akshat, Sakshi this side.
Can you share your video which you uploaded for the Upgrad's internship.
My whatsapp is not working, that's why I am emailing you.
Please share if you can.
"""
list = []

for i in content[::-1]:
  store = i
  list.append(store)

content2 = ''.join(list)
content2 = [content2,'Segment-4/contacts.csv']

yag = yagmail.SMTP(user = sender, password=os.getenv("PASSWORD"))
yag.send(to = receiver,subject=subject,contents=content2)

print("Email sent!")

