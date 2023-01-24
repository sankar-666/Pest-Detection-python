from flask import *
from database import *


admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')