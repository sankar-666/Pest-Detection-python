from flask import *
from database import *


farmer=Blueprint('farmer',__name__)

@farmer.route('/farmerhome')
def farmerhome():
    return render_template('farmerhome.html')