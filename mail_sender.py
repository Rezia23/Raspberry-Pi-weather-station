# -*- coding: utf-8 -*-
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def email():
	#nastaveni prijemce a odesilatele
	sender_email = "raspberry141.3@gmail.com"
	receiver_email = "reciever@domain.com"
	password = "raspberry3B+"

	#nastaveni jednotlivych casti e-mailu
	body = "Hello,\nthis is your yesterday\'s weather summary."
	message = MIMEMultipart()
	message["From"] = "Raspberry Pi weather station"
	message["To"] = "You"
	message["Subject"] = "Weather " + str(datetime.datetime.now())
	message.attach(MIMEText(body, "plain"))

	filename = "graph.svg"

	#nacteni a zakodovani souboru
	with open(filename, "rb") as attachment:
    		part = MIMEBase("application", "octet-stream")
    		part.set_payload(attachment.read())
	encoders.encode_base64(part)


	#Nastaveni hlavicky a pripojeni zpravy jako string
	part.add_header(
    		"Content-Disposition",
    		"attachment; filename= weather_graph.svg",
	)
	message.attach(part)
	text = message.as_string()

	#Prihlaseni a zaslani emailu
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    		server.login(sender_email, password)
    		server.sendmail(sender_email, receiver_email, text)
