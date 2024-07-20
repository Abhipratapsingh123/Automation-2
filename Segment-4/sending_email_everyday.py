import yagmail
import os
import time
from datetime import datetime as dt
import pytz

sender = 'fee.mca@gmail.com'
receiver = 'abhi.pratap@gmail.com'

subject = 'Upgrad video'

content = """
Received?
"""

# Replace 'Asia/Kolkata' with your local time zone
local_tz = pytz.timezone('Asia/Kolkata')

while True:
  now = dt.now(local_tz)
  if now.hour == 17 and now.minute == 53:
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=content)
    print("Email sent")
    time.sleep(60)
