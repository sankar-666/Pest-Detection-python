from flask import *
from database import *


customer=Blueprint('customer',__name__)

@customer.route('/customerhome')
def customerhome():
    return render_template('customerhome.html')