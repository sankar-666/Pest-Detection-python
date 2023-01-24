from flask import *
from database import *


public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
    return render_template('home.html')


@public.route('/login',methods=['post','get'])
def login():

    if 'btn' in request.form:
        uname=request.form['uname']
        pasw =request.form['pasw']

        q="select * from login where username='%s' and password='%s'"%(uname,pasw)
        res=select(q)


        if res:
            session['loginid']=res[0]["login_id"]
            utype=res[0]["usertype"]
            if utype == "admin":
                return redirect(url_for("admin.adminhome"))
            elif utype == "stationmaster":
                q="select * from stationmaster where login_id='%s'"%(session['loginid'])
                val=select(q)
                if val:
                    session['stid']=val[0]['smaster_id']
                    return redirect(url_for("stationmaster.stationmasterhome"))
               
            
            else:
                flash("failed try again")
                return redirect(url_for("public.login"))


    return render_template("login.html")



@public.route('/customerreg',methods=['get','post'])
def customerreg():

    if 'btn' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        hname=request.form['hname']
        place=request.form['place']
        pin=request.form['pin']
        phone=request.form['phone']
        email=request.form['email'] 
        uname=request.form['uname'] 
        passw=request.form['passw'] 

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into `login` values(NULL,'%s','%s','customer')"%(uname,passw)
            res=insert(q)

            w="insert into customer value(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,hname,place,pin,phone,email)
            insert(w)
            flash("Registration Successfull")
            return redirect(url_for("public.login"))

    return render_template("customerreg.html")



@public.route('/farmerreg',methods=['get','post'])
def farmerreg():

    if 'btn' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        hname=request.form['hname']
        place=request.form['place']
        pin=request.form['pin']
        phone=request.form['phone']
        date=request.form['date']
        gender=request.form['gender']
        uname=request.form['uname'] 
        passw=request.form['passw'] 

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into `login` values(NULL,'%s','%s','farmer')"%(uname,passw)
            res=insert(q)

            w="insert into farmer value(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,hname,place,pin,phone,gender,date)
            insert(w)
            flash("Registration Successfull")
            return redirect(url_for("public.login"))

    return render_template("farmerreg.html")