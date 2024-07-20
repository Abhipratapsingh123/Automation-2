import smtplib
import os

sender = "fee.mca941@gmail.com"
receiver = "abhi.pratap9667@gmail.com"

# Ensure environment variable PASSWORD-2 is set
password = os.getenv("PASSWORD-2")
if password is None:
    print("ERROR: Environment variable PASSWORD-2 is not set. Please set it before running the script.")
    exit(1)  # Exit with an error code

message = """\
Subject: Hello Hello

This is Abhi!
Just wanted to say hi!
"""

# Use smtplib.SMTP_SSL for secure connection (recommended)
server = smtplib.SMTP_SSL('smtp.office365.com', 465)  # Use port 465 for SSL

try:
    # Login with sender email and password
    server.login(sender, password)

    # Send the email
    server.sendmail(sender, receiver, message)
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)
finally:
    # Always close the connection
    server.quit()
print("Email sent!")