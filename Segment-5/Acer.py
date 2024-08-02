from selenium import webdriver
import time

import yagmail
import os

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blank-features = AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.flipkart.com/acer-aspire-7-2023-intel-core-i5-12th-gen-12450h-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-144-hz-a715-76g-gaming-laptop/p/itm33a41661dc40d?pid=COMGP8QVTK3EQDXE&cmpid=product.share.pp&_refId=PP.9adad02b-0463-48ae-8e41-1a2b7f0598fa.COMGP8QVTK3EQDXE&_appId=WA")
    return driver



def clean_text(text):
    """Extract only the required value from text"""
    output = text.split("₹")[1]
    output = output.replace(",", "")
    return int(output)


def send_email(price):
    sender = os.getenv('EMAIL_SENDER')
    receiver = os.getenv('EMAIL_RECEIVER')

    subject = "Khareed le ab"


    contents = f"""
    The price of the laptop today is {price}
    """


    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")



def main():
    driver = get_driver()
    time.sleep(2)
    element=driver.find_element(by="xpath",value='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]')
    text = element.text
    cleaned_text = clean_text(text)
    # text = str(clean_text(element.text))
    send_email(cleaned_text)

main()
