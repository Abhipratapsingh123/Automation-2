import re

text = "Hi there you here example@example.com some  more text here  and there another@example.de "

pattern = re.compile("[a-z]+@[a-z]+.[a-z]+")

matches = pattern.findall(text)

print(matches)


# Enough for this, no use