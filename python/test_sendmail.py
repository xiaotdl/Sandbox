# Ref:
# https://en.wikibooks.org/wiki/Python_Programming/Email

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

SENDER_USER = 'xiaotian.li.robot@gmail.com'
SENDER_PWD = 'robot123'

def sendmail(receiver, subject, body):
    fromaddr = SENDER_USER
    toaddrs  = [receiver]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddrs[0]
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    print "== Sending Email ==\n"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user=SENDER_USER, password=SENDER_PWD)
        text = msg.as_string()
        print text
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    print "\n== Email sent succesffully =="

if __name__ == "__main__":
    sendmail('xiaotdl@gmail.com', '<test subject>', '<test body>')

# >>>
# == Sending Email ==
# Content-Type: multipart/mixed; boundary="===============2800599854358151708=="
# MIME-Version: 1.0
# From: xiaotian.li.robot@gmail.com
# To: xiaotdl@gmail.com
# Subject: <test subject>

# --===============2800599854358151708==
# Content-Type: text/plain; charset="us-ascii"
# MIME-Version: 1.0
# Content-Transfer-Encoding: 7bit

# <test body>
# --===============2800599854358151708==--

# == Email sent succesffully ==
