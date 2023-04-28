from flask import *
from database import *

api=Blueprint('api',__name__)




@api.route("/login")
def login():
	data={}

	uname=request.args['username']
	pwd=request.args['password']


	print(uname,pwd)
	q="select * from login where username='%s' and password='%s'"%(uname,pwd)
	res=select(q)
	if res:
		
		data['status']='success'
		data['data']=res
	else:
		data['status']='failed'
	return str(data)

@api.route("/customerreg")
def customerreg():
    data={}

    fname=request.args['fname']
    lname=request.args['lname']
    hname=request.args['hname']
    place=request.args['place']
    pin=request.args['pincode']
    phone=request.args['phone']
    email=request.args['email'] 
    uname=request.args['username'] 
    passw=request.args['password'] 

    q="select * from login where username='%s'"%(uname)
    res=select(q)
    if res:
        data['status']='duplicate'
    else:
        q="insert into `login` values(NULL,'%s','%s','customer')"%(uname,passw)
        res=insert(q)

        w="insert into customer value(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,hname,place,pin,phone,email)
        insert(w)
        flash("Registration Successfull")
        data['status']='success'

    return str(data)


@api.route('/viewpest')
def viewpest():
    data={}
    q="select * from pest"
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="viewpest"
    return str(data)

@api.route('/viewharmfull_pest')
def viewharmfull_pest():
    data={}
    q="SELECT *,harmfull.details as details FROM pest,`harmfull`,`crops` WHERE `pest`.pest_id=`harmfull`.pest_id AND `harmfull`.crop_id=`crops`.`crop_id`"
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="viewharmfull_pest"
    return str(data)


@api.route('/view_pesticides')
def view_pesticides():
    data={}
    hid=request.args['hid']
    q="SELECT * FROM `pesticide` WHERE harmfull_id IN (SELECT harmfull_id FROM `harmfull` ) and harmfull_id='%s'"%(hid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="view_pesticides"
    return str(data)


@api.route('/pesticide_addtocart')
def pesticide_addtocart():
    data={}
    amt=request.args['amt']
    pesid=request.args['pesid'] 
    rstock = request.args['rstock']
    lid = request.args['lid']
    total = int(amt) * int(rstock)

    q="select * from pordermaster where p_status='pending' and customer_id=(select customer_id from customer where login_id='%s')"%(lid)
    res=select(q)
    if res:
        oid=res[0]['pordermaster_id']
    else:
        q="insert into pordermaster values(null,(select customer_id from customer where login_id='%s'),curdate(),0,'pending')"%(lid)
        oid=insert(q)
    q="select * from porderdetails where pesticide_id='%s' and pordermaster_id='%s'"%(pesid,oid)
    val=select(q)
    if val:
        q="update porderdetails set pquantity=pquantity+'%s', p_total=p_total+'%s' where pesticide_id='%s' and pordermaster_id='%s' "%(rstock,total,pesid,oid)
        update(q)
    else:
        q="insert into porderdetails values (null,'%s','%s','%s','%s','pending')"%(oid,pesid,rstock,total)
        insert(q)
    q="update pordermaster set p_amount=p_amount+'%s' where pordermaster_id='%s'"%(total,oid)
    update(q)
    data['status']="success"
    data['method']="pesticide_addtocart"
    return str(data)



@api.route('/view_pesticide_cart')
def view_pesticide_cart():
    data={}
    lid=request.args['lid']
    q="SELECT * FROM `pordermaster`,`porderdetails`,`pesticide` WHERE `pordermaster`.pordermaster_id=`porderdetails`.pordermaster_id AND `porderdetails`.pesticide_id=`pesticide`.pesticide_id  and pordermaster.p_status='pending' and pordermaster.customer_id=(select customer_id from customer where login_id='%s')"%(lid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="view_pesticide_cart"
    return str(data)

@api.route('/pesticide_payment')
def pesticide_payment():
    data={}
    pmid=request.args['pmid']
    amount=request.args['amount']
    q="insert into payment values (null,'%s','pesticide','%s',curdate())"%(pmid,amount)
    insert(q)
    q="update pordermaster set p_status='payment completed'  where pordermaster_id='%s'"%(pmid)
    update(q)

    data['status']="success"

    data['method']="pesticide_payment"
    return str(data)



@api.route('/view_pesticide_history')
def view_pesticide_history():
    data={}
    lid=request.args['lid']
    q="SELECT * FROM `pordermaster`,`porderdetails`,`pesticide` WHERE `pordermaster`.pordermaster_id=`porderdetails`.pordermaster_id AND `porderdetails`.pesticide_id=`pesticide`.pesticide_id   and pordermaster.customer_id=(select customer_id from customer where login_id='%s')"%(lid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="view_pesticide_history"
    return str(data)




@api.route('/item_addtocart')
def item_addtocart():
    data={}
    iid=request.args['iid']
    rstock = request.args['rstock']
    amt = request.args['amt']
    lid = request.args['lid']
    total = int(amt) * int(rstock)

    q="select * from ordermaster where order_status='pending' and customer_id=(select customer_id from customer where login_id='%s')"%(lid)
    res=select(q)
    if res:
        oid=res[0]['ordermaster_id']
    else:
        q="insert into ordermaster values(null,(select customer_id from customer where login_id='%s'),0,curdate(),'pending')"%(lid)
        oid=insert(q)
    q="select * from orderdetails where item_id='%s' and ordermaster_id='%s'"%(iid,oid)
    val=select(q)
    if val:
        q="update orderdetails set quantity=quantity+'%s', total_amount=total_amount+'%s' where item_id='%s' and ordermaster_id='%s' "%(rstock,total,iid,oid)
        update(q)
    else:
        q="insert into orderdetails values (null,'%s','%s','%s','%s','pending')"%(oid,iid,rstock,total)
        insert(q)
    q="update ordermaster set totalamount=totalamount+'%s' where ordermaster_id='%s'"%(total,oid)
    update(q)
    data['status']="success"
    data['method']="item_addtocart"
    return str(data)

@api.route('/viewitem')
def viewitem():
    data={}
    # hid=request.args['hid']
    q="SELECT * FROM item"
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="viewitem"
    return str(data)

@api.route('/view_item_cart')
def view_item_cart():
    data={}
    lid=request.args['lid']
    q="SELECT * FROM `ordermaster`,`orderdetails`,`item`,`farmer` WHERE `ordermaster`.ordermaster_id=`orderdetails`.ordermaster_id AND `orderdetails`.item_id=`item`.item_id AND `item`.farmer_id=`farmer`.farmer_id  and ordermaster.order_status='pending' and ordermaster.customer_id=(select customer_id from customer where login_id='%s')"%(lid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="view_item_cart"
    return str(data)


@api.route('/item_payment')
def item_payment():
    data={}
    omid=request.args['pmid']
    amount=request.args['amount']
    q="insert into payment values (null,'%s','item','%s',curdate())"%(omid,amount)
    insert(q)
    q="update ordermaster set order_status='payment completed'  where ordermaster_id='%s'"%(omid)
    update(q)

    data['status']="success"

    data['method']="item_payment"
    return str(data)



@api.route('/view_item_history')
def view_item_history():
    data={}
    lid=request.args['lid']
    q="SELECT * FROM `ordermaster`,`orderdetails`,`item`,`farmer` WHERE `ordermaster`.ordermaster_id=`orderdetails`.ordermaster_id AND `orderdetails`.item_id=`item`.item_id AND `item`.farmer_id=`farmer`.farmer_id  and ordermaster.order_status <> 'pending' and ordermaster.customer_id=(select customer_id from customer where login_id='%s')"%(lid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="view_item_history"
    return str(data)




@api.route("/addcomplaint")
def addcomplaint():
    complaint=request.args['complaint']
    lid=request.args['lid']
   
    data={}

    q="insert into complaint values (null,(select customer_id from customer where login_id='%s'),'%s','pending',curdate())"%(lid,complaint)
    insert(q)
    data['status']="success"
    data['method']="addcomplaint"
    return str(data)
  
    
@api.route('/viewcomplaint')
def viewcomplaint():
    data={}
    lid=request.args['lid']
    z="select * from complaint where customer_id= (select customer_id from customer where login_id='%s')"%(lid)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="viewcomplaint"
    return str(data)


@api.route('/viewenquiry')
def viewenquiry():
    data={}
    lid=request.args['lid']
    z="select * from enquiry where customer_id=(select customer_id from customer where login_id='%s')"%(lid)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="viewenquiry"
    return str(data)

@api.route('/viewfarmers')
def viewfarmers():
    data={}
    # lid=request.args['lid']
    z="select *,concat(fname,'',lname) as farmername from farmer"
    res=select(z)
    print(select(z))

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="viewfarmers"
    return str(data)


@api.route("/addenquiry")
def addenquiry():
    complaint=request.args['complaint']
    lid=request.args['lid']
    fid=request.args['fid']
   
    data={}

    q="insert into enquiry values (null,(select customer_id from customer where login_id='%s'),'%s','%s','pending',curdate())"%(lid,fid,complaint)
    insert(q)
    data['status']="success"
    data['method']="addenquiry"
    return str(data)
