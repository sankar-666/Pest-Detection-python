from flask import Flask
from public import public
from farmer import farmer
from admin import admin
from customer import customer
from api import api


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

app=Flask(__name__)
app.secret_key="pest"
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(farmer,url_prefix="/farmer")
app.register_blueprint(customer,url_prefix="/customer")
app.register_blueprint(api,url_prefix="/api")
app.register_blueprint(public)


mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_mail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


app.run(debug=True,port=5083,host="0.0.0.0")
