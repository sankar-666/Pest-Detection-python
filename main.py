from flask import Flask
from public import public
from farmer import farmer
from admin import admin
from customer import customer

app=Flask(__name__)
app.secret_key="prayulla"
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(farmer,url_prefix="/farmer")
app.register_blueprint(customer,url_prefix="/customer")
app.register_blueprint(public)


app.run(debug=True,port=5083,host="0.0.0.0")