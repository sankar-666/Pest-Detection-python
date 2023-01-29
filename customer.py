from flask import *
from database import *


customer=Blueprint('customer',__name__)

@customer.route('/customerhome')
def customerhome():
    return render_template('customerhome.html')

@customer.route('/customer_view_pest')
def customer_view_pest():
    data={}
    q="select * from pest"
    data['res']=select(q)
    return render_template('customer_view_pest.html',data=data)



@customer.route('/customer_view_harmfullpest')
def customer_view_harmfullpest():
    data={}
    q="SELECT *,harmfull.details as details FROM pest,`harmfull`,`crops` WHERE `pest`.pest_id=`harmfull`.pest_id AND `harmfull`.crop_id=`crops`.`crop_id`"
    data['res']=select(q)
    return render_template('customer_view_harmfullpest.html',data=data)


@customer.route('/customer_view_pesticides')
def customer_view_pesticides():
    data={}
    hid=request.args['hid']
    pest=request.args['pest']
    q="SELECT * from pesticide where harmfull_id='%s'"%(hid)
    data['res']=select(q)
    return render_template('customer_view_pesticides.html',data=data,pest=pest)


@customer.route('/customer_view_items')
def customer_view_items():
    data={}
    q="SELECT * from item inner join farmer using (farmer_id)"
    data['res']=select(q)
    return render_template('customer_view_items.html',data=data)


@customer.route('/add_to_cart',methods=['get','post'])
def add_to_cart():
    data={}
    iid=request.args['iid']
    cp=request.args['cp']
    mu=request.args['mu']
    item=request.args['item']
    stock=request.args['stock']

    if 'btn' in request.form:
        total = request.form['total']
        rstock = request.form['rstock']

        q="select * from ordermaster where order_status='pending' and customer_id='%s'"%(session['cid'])
        res=select(q)
        if res:
            oid=res[0]['ordermaster_id']
        else:
            q="insert into ordermaster values(null,'%s',0,curdate(),'pending')"%(session['cid'])
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
        flash("Successfully added to Cart")
        return redirect(url_for("customer.customer_view_items"))

   
    return render_template('add_to_cart.html',data=data,item=item,cp=cp,mu=mu,stock=stock)




@customer.route('/cart')
def cart():
    data={}
    q="SELECT * FROM `ordermaster`,`orderdetails`,`item`,`farmer` WHERE `ordermaster`.ordermaster_id=`orderdetails`.orderdetails_id AND `orderdetails`.item_id=`item`.item_id AND `item`.farmer_id=`farmer`.farmer_id  and ordermaster.order_status='pending' and ordermaster.customer_id='%s'"%(session['cid'])
    data['res']=select(q)

    return render_template('cart.html',data=data)


@customer.route('/customer_my_orders')
def customer_my_orders():
    data={}
    q="SELECT * FROM `ordermaster`,`orderdetails`,`item`,`farmer` WHERE `ordermaster`.ordermaster_id=`orderdetails`.orderdetails_id AND `orderdetails`.item_id=`item`.item_id AND `item`.farmer_id=`farmer`.farmer_id  and ordermaster.customer_id='%s'"%(session['cid'])
    data['res']=select(q)

    return render_template('customer_my_orders.html',data=data)


@customer.route('/customer_make_payment',methods=['get','post'])
def customer_make_payment():
    data={}
    omid=request.args['omid']
    amount=request.args['amount']
    if 'btn' in request.form:
        q="insert into payment values (null,'%s','%s',curdate())"%(omid,amount)
        insert(q)
        q="update ordermaster set order_status='payment completed'  where ordermaster_id='%s'"%(omid)
        update(q)
        flash("Payment Completed")
        return redirect(url_for("customer.customerhome"))
    return render_template('customer_make_payment.html',data=data,total=amount)




@customer.route("/customer_send_complaint",methods=['get','post'])
def customer_send_complaint():
    data={}

    cid=session['cid']

    if 'btn' in request.form:
        comp=request.form['comp']

        q="insert into complaint values(NULL,'%s','%s','pending',curdate())"%(cid,comp)
        print(q)
        insert(q)
        return redirect(url_for("customer.customer_send_complaint"))
    
    q="select * from complaint where customer_id='%s'"%(cid)
    data['res']=select(q)
    return render_template("customer_send_complaint.html",data=data)



@customer.route("/customer_add_enquiry",methods=['get','post'])
def customer_add_enquiry():
    data={}

    cid=session['cid']

    if 'btn' in request.form:
        comp=request.form['comp']

        q="insert into enquiry values(NULL,'%s',0,'%s','pending',curdate())"%(cid,comp)
        print(q)
        insert(q)
        return redirect(url_for("customer.customer_add_enquiry"))
    
    q="select * from enquiry where customer_id='%s'"%(cid)
    data['res']=select(q)
    return render_template("customer_add_enquiry.html",data=data)