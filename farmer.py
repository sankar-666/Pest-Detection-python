from flask import *
from database import *
from newcnn import *
import cv2

farmer=Blueprint('farmer',__name__)

@farmer.route('/farmerhome')
def farmerhome():
    data={}
    fname=session['fname']
    data['fname']=fname
    return render_template('farmerhome.html',data=data)



@farmer.route('/farmer_view_pest')
def farmer_view_pest():
    data={}
    q="select * from pest"
    data['res']=select(q)
    return render_template('farmer_view_pest.html',data=data)



@farmer.route('/farmer_view_harmfullpest')
def farmer_view_harmfullpest():
    data={}
    q="SELECT *,harmfull.details as details FROM pest,`harmfull`,`crops` WHERE `pest`.pest_id=`harmfull`.pest_id AND `harmfull`.crop_id=`crops`.`crop_id`"
    data['res']=select(q)
    return render_template('farmer_view_harmfullpest.html',data=data)


@farmer.route('/farmer_view_pesticides')
def farmer_view_pesticides():
    data={}
    hid=request.args['hid']
    pest=request.args['pest']
    # q="SELECT * from pesticide where harmfull_id='%s'"%(hid)
    q="SELECT *,pesticide.image as image FROM `pesticide` INNER JOIN `harmfull` USING (harmfull_id) INNER JOIN `pest` USING (pest_id) where pest='%s'"%(pest)
    data['res']=select(q)
    return render_template('farmer_view_pesticides.html',data=data,pest=pest)


@farmer.route('/farmer_view_farmingtyes')
def farmer_view_farmingtyes():
    data={}
    q="SELECT * from farmingtype"
    data['res']=select(q)
    return render_template('farmer_view_farmingtyes.html',data=data)

import uuid
@farmer.route('/farmer_manage_items',methods=['get','post'])
def farmer_manage_items():
    data={}
    ftid=request.args['ftid']
    data['ftid']=ftid
    if 'btn' in request.form: 
        item=request.form['item']
        stock=request.form['stock']
        munit=request.form['munit']
        cpunit=request.form['cpunit']
        image=request.files['image']
        path="static/uploads/"+str(uuid.uuid4())+image.filename
        image.save(path)
        
    
        q="insert into item values (null,'%s','%s','%s','%s','%s','%s','%s')"%(session['fid'],ftid,item,path,stock,munit,cpunit)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("farmer.farmer_manage_items",ftid=ftid))

  
    q="SELECT * from item where farmingtype_id='%s' and farmer_id='%s'"%(ftid,session['fid'])
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        iid=request.args['iid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from item where item_id='%s'"%(iid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
        
            item=request.form['item']
            stock=request.form['stock']
            # munit=request.form['munit']
            cpunit=request.form['cpunit']
            if request.files['image']:
                image=request.files['image']
                path="static/uploads/"+str(uuid.uuid4())+image.filename
                image.save(path)
                q="update item set item='%s', item_image='%s', stock='%s',  costper_unit='%s' where item_id='%s'"%(item,path,stock,cpunit,iid)
            else:
                q="update item set item='%s',  stock='%s',  costper_unit='%s' where item_id='%s'"%(item,stock,cpunit,iid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("farmer.farmer_manage_items",ftid=ftid))
    if action == "delete":
        q="delete from item where item_id='%s' "%(iid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("farmer.farmer_manage_items",ftid=ftid))

    
    
    return render_template('farmer_manage_items.html',data=data)



@farmer.route('/farmer_view_training')
def farmer_view_training():
    data={}
    q="SELECT * from traning"
    data['res']=select(q)
    return render_template('farmer_view_training.html',data=data)


@farmer.route('/farmer_view_orders')
def farmer_view_orders():
    data={}
    q="SELECT * FROM `ordermaster`,`orderdetails`,`item`,`customer` WHERE `ordermaster`.ordermaster_id=`orderdetails`.ordermaster_id AND `orderdetails`.item_id=`item`.item_id AND `ordermaster`.customer_id=`customer`.customer_id AND item.farmer_id='%s'"%(session['fid'])
    print(q)
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid'] 
    else:
        action=None
    
    if action == "confirm":
        q="update ordermaster set order_status='payment confirmed' where ordermaster_id='%s'"%(omid)
     
        update(q)
        return redirect(url_for("farmer.farmer_view_orders"))
    
    if action == "dispatch":
        q="update ordermaster set order_status='Delivery Completed' where ordermaster_id='%s'"%(omid)
        update(q)
        return redirect(url_for("farmer.farmer_view_orders"))
    return render_template('farmer_view_orders.html',data=data)


@farmer.route('/farmer_view_payment')
def farmer_view_payment():
    omid=request.args['omid']
    data={}
    q="select * from payment where ordermaster_id='%s' and type='item'"%(omid)
    data['res']=select(q)

    

    return render_template('farmer_view_payment.html',data=data)


@farmer.route('/farmer_view_enquiry',methods=['get','post'])
def farmer_view_enquiry():
    data={}
    q="select * from enquiry inner join customer using (customer_id) where farmer_id='%s'"%(session['fid'])
    res=select(q)
    data['res']=res

    for i in range(1,len(res)+1):
        if 'btn'+str(i) in request.form:
            enq_id=request.form['enq'+str(i)]
            reply=request.form['reply'+str(i)]
            q="update enquiry set enquiry_reply='%s',farmer_id='%s' where enquiry_id='%s'"%(reply,session['fid'],enq_id)
            update(q)
            return redirect(url_for("farmer.farmer_view_enquiry"))
    return render_template('farmer_view_enquiry.html',data=data)

import uuid
@farmer.route('/farmer_predict_pest',methods=['get','post'])
def farmer_predict_pest():
    data={}
    hid=""
    pest=""
    q="select * from crops"
    data['crops']=select(q)
    out ="No specifice output"
    if 'btn' in request.form:
        image=request.files['image']
        crop=request.form['crop']
        path="static/prediction/test.png"
        image.save(path)
        val=predictcnn()
        if val == 0:
            out="Aphids"
        elif val ==1:
            out="Armyworms"
        elif val ==2:
            out="Beetle"
        elif val ==3:
            out="Bollworm"
        elif val ==4:
            out="Grasshopper"
        elif val ==5:
            out="Mites"
        elif val ==6:
            out="Mosqito"
        elif val ==7:
            out="Sawfly"
        elif val ==8:
            out="Stem borer"

        q="SELECT * FROM pest INNER JOIN harmfull USING (pest_id) INNER JOIN crops USING (crop_id) where pest like '%s' and crop like '%s'"%(out,crop)
        print(q) 
        res=select(q)
        if res:
            data['outcome']=res[0]['crop']
            hid=res[0]['harmfull_id']
            pest=res[0]['pest']
            print(hid)
            print(pest)
    
        data['showHide']=True
        print("Output: ",out)
    return render_template('farmer_predict_pest.html',data=data,out=out,hid=hid,pest=pest)




@farmer.route('/add_to_cart_pesticide',methods=['get','post'])
def add_to_cart_pesticide():
    data={}
    pes=request.args['pes']
    amt=request.args['amt']
    pesid=request.args['pesid']

    if 'btn' in request.form:
        total = request.form['total']
        rstock = request.form['rstock']

        q="select * from pordermaster where p_status='pending' and customer_id='%s'"%(session['loginid'])
        res=select(q)
        if res:
            oid=res[0]['pordermaster_id']
        else:
            q="insert into pordermaster values(null,'%s',curdate(),0,'pending')"%(session['loginid'])
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
        flash("Successfully added to Cart")
        return redirect(url_for("farmer.farmerhome"))

   
    return render_template('add_to_cart_pesticide.html',data=data,pes=pes,amt=amt)


@farmer.route('/farmer_cart')
def farmer_cart():
    data={}
    q="SELECT * FROM `pordermaster`,`porderdetails`,`pesticide` WHERE `pordermaster`.pordermaster_id=`porderdetails`.pordermaster_id AND `porderdetails`.pesticide_id=`pesticide`.pesticide_id  and pordermaster.p_status='pending' and pordermaster.customer_id='%s'"%(session['loginid'])
    data['res']=select(q)

    return render_template('farmer_cart.html',data=data)

@farmer.route('/farmer_make_payment',methods=['get','post'])
def farmer_make_payment():
    data={}
    pmid=request.args['pmid']
    amount=request.args['amount']
    if 'btn' in request.form:
        q="insert into payment values (null,'%s','pesticide','%s',curdate())"%(pmid,amount)
        insert(q)
        q="update pordermaster set p_status='payment completed'  where pordermaster_id='%s'"%(pmid)
        update(q)
        flash("Payment Completed")
        return redirect(url_for("farmer.farmerhome"))
    return render_template('farmer_make_payment.html',data=data,total=amount)




@farmer.route('/farmer_view_mybokkings')
def farmer_view_mybokkings():
    data={}
    q="SELECT * FROM `pordermaster`,`porderdetails`,`pesticide` WHERE `pordermaster`.pordermaster_id=`porderdetails`.pordermaster_id AND `porderdetails`.pesticide_id=`pesticide`.pesticide_id  and  pordermaster.customer_id='%s'"%(session['loginid'])
    data['res']=select(q)

    return render_template('farmer_view_mybokkings.html',data=data)


@farmer.route('/more_pest_details')
def more_pest_details():
    data={}
    pest='%'+request.args['pest']+'%'
    q="SELECT * FROM pest where pest like '%s'"%(pest)
    data['res']=select(q)

    return render_template('more_pest_details.html',data=data)