from selenium.webdriver.common.virtual_authenticator import required_virtual_authenticator
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return "WelcomeMF"

@app.route('/insidehome')
def inside_home():
  return "You are in the home"
app.run(host = '0.0.0.0')