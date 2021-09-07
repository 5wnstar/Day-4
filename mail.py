import smtplib

sender = 'admin@admin.com'
receivers = ['guest@guest.com']

message = """From: From Person <admin@admin.com>
To: To Person <guest@guest.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
