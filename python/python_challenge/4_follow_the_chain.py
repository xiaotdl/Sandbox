import re
import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
r = requests.get(url)
print r.content
# >>>
# 'and the next nothing is 44827'
while True:
    # re.DOTALL flag tells python to make the '.' special character match all characters, including newline characters.
    m1 = re.match(".*and the next nothing is (\d+)", r.content, re.DOTALL)
    # To match ==>
    # Yes. Divide by two and keep going.
    m2 = re.match(".*Divide by two and keep going.", r.content)
    if m1:
        next_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + m1.group(1)
        print next_url
        r = requests.get(next_url)
        print r.content
    elif m2:
        last_nothing = r.request.url[len("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="):]
        next_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(int(last_nothing) / 2)
        print next_url
        r = requests.get(next_url)
        print r.content
    else:
        raise Exception("No match: " + r.content)

# >>>
# Traceback (most recent call last):
#       File "4_follow_the_chain.py", line 27, in <module>
#           raise Exception("No match: " + r.content)
#       Exception: No match: peak.html
