from flask import Flask
from flask.ext.mail import Mail
from flask.ext.mail import Message

app =Flask(__name__)
mail=Mail(app)

app.config.update(
	DEBUG= True,
	MAIL_SERVER= 'smtp.gmail.com',
	MAIL_PORT= 587,
	MAIL_USE_SSL= False,
	MAIL_USE_TLS= True,
	MAIL_USERNAME = 'eniqqo8181@gmail.com',
	MAIL_PASSWORD = 'AIKOnikolas'
	)

mail=Mail(app)

@app.route("/")
def index():
	msg = Message(
              'Hello',
	       sender='eniqqo8181@gmail.com',
	       recipients=
               ['eniqqo8181@gmail.com'])
	msg.body = "This is the email body"
	mail.send(msg)
	
def hello_world():
    return 'Hola Profesor Jorge Neyra!'
if __name__ == '__main__':
    app.run(host='0.0.0.0')
