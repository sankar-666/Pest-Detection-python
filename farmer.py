from flask import *
from database import *
from newcnn import *
import cv2

farmer=Blueprint('farmer',__name__)

@farmer.route('/farmerhome')
def farmerhome():
    return render_template('farmerhome.html')



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
    q="SELECT * from pesticide where harmfull_id='%s'"%(hid)
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
    q="select * from `ordermaster`,`orderdetails`,`item`,`customer` where `ordermaster`.ordermaster_id=`orderdetails`.orderdetails_id and `orderdetails`.item_id=`item`.item_id and `ordermaster`.customer_id=`customer`.customer_id and item.farmer_id='%s'"%(session['fid'])
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
    q="select * from payment where ordermaster_id='%s'"%(omid)
    data['res']=select(q)

    

    return render_template('farmer_view_payment.html',data=data)


@farmer.route('/farmer_view_enquiry',methods=['get','post'])
def farmer_view_enquiry():
    data={}
    q="select * from enquiry inner join customer using (customer_id)"
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
    out ="No specifice output"
    if 'btn' in request.form:
        image=request.files['image']
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

        q="SELECT * FROM pest INNER JOIN harmfull USING (pest_id) INNER JOIN crops USING (crop_id) where pest like '%s'"%(out)
        res=select(q)
        if res:
            data['outcome']=res[0]['crop']
    
        data['showHide']=True
        print("Output: ",out)
    return render_template('farmer_predict_pest.html',data=data,out=out)