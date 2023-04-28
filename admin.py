from flask import *
from database import *

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail


admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@admin.route('/adminviewfarmers') 
def adminviewfarmers():
    data={}
    q="select * from farmer inner join login using(login_id)"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        login_id=request.args['login_id'] 
    else:
        action=None

        
    if action == "accept":
       
        q="select * from farmer where login_id='%s'"%(login_id)
        res=select(q)
        if res:
            emailid=res[0]['email']
            email=emailid
            print(email)
            
            pwd="Your Registration request has been Accepted, you can Now Login with your Username and Password.......!"
            
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('projectsriss2020@gmail.com','vroiyiwujcvnvade')
            
            except Exception as e:
                print("Couldn't setup email!!"+str(e))

            pwd = MIMEText(pwd)

            pwd['Subject'] = 'Approval Request'

            pwd['To'] = email

            pwd['From'] = 'projectsriss2020@gmail.com'
                
            try:
                gmail.send_message(pwd)

                flash("EMAIL SENED SUCCESFULLY")



            except Exception as e:
                print("COULDN'T SEND EMAIL", str(e))
            else:
                flash('ADDED...')
                q="update login set usertype='farmer' where login_id='%s'"%(login_id)
                update(q)
    
        return redirect(url_for("admin.adminviewfarmers"))
    
    if action == "reject":
        q="update login set usertype='reject' where login_id='%s' "%(login_id)
        update(q)
        q="select * from farmer where login_id='%s'"%(login_id)
        email=select(q)[0]['email']
        pwd="Your Registration request has been Rejected.........!"

        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('projectsriss2020@gmail.com','vroiyiwujcvnvade')
        except Exception as e:
            print("Couldn't setup email!!"+str(e))

        pwd = MIMEText(pwd)

        pwd['Subject'] = 'Approval Request'

        pwd['To'] = email

        pwd['From'] = 'projectsriss2020@gmail.com'

        try:
            gmail.send_message(pwd)

            flash("Rejected Successfully")
            


        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        else:
            flash("INVALID DETAILS")
        flash("rejected Successfully")
        return redirect(url_for("admin.adminviewfarmers"))
    
    

    return render_template('adminviewfarmers.html',data=data)


@admin.route('/adminviewcustomers')
def adminviewcustomers():
    data={}
    q="select * from customer"
    data['res']=select(q)
    return render_template('adminviewcustomers.html',data=data)


@admin.route('/adminviewmarketitems')
def adminviewmarketitems():
    data={}
    q="select * from item inner join farmer using (farmer_id)"
    data['res']=select(q)
    return render_template('adminviewmarketitems.html',data=data)


@admin.route('/admin_manage_farmingtypes',methods=['get','post'])
def admin_manage_farmingtypes():
    data={}
    if 'btn' in request.form:
        ftype=request.form['ftype']
        
    
        q="insert into farmingtype values (null,'%s')"%(ftype)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_farmingtypes"))

    data={}
    q="select * from farmingtype"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        ft_id=request.args['ft_id'] 
    else:
        action=None

    
    if action == "update":
        q="select * from farmingtype where farmingtype_id='%s'"%(ft_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            ftype=request.form['ftype']

            q="update farmingtype set farmingtype_name='%s' where farmingtype_id='%s' "%(ftype,ft_id)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_farmingtypes"))
    if action == "delete":
        q="delete from farmingtype where farmingtype_id='%s' "%(ft_id)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_farmingtypes"))
    return render_template('admin_manage_farmingtypes.html',data=data) 



@admin.route('/admin_manage_events',methods=['get','post'])
def admin_manage_events():
    data={}
    if 'btn' in request.form:
        title=request.form['title']
        desc=request.form['desc']
        date=request.form['date']
        venue=request.form['venue']
        
    
        q="insert into event values (null,'%s','%s','%s','%s','pending')"%(title,desc,date,venue)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_events"))

    data={}
    q="select * from event"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        eid=request.args['eid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from event where event_id='%s'"%(eid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            title=request.form['title']
            desc=request.form['desc']
            date=request.form['date']
            venue=request.form['venue']

            q="update event set event_title='%s', event_desc='%s', event_venue='%s', event_date='%s' where event_id='%s' "%(title,desc,venue,date,eid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_events"))
    if action == "delete":
        q="delete from event where event_id='%s' "%(eid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_events"))
    return render_template('admin_manage_events.html',data=data) 




@admin.route('/admin_manage_pest',methods=['get','post'])
def admin_manage_pest():
    data={}
    if 'btn' in request.form:
        pest=request.form['pest']
        details=request.form['details']
        image=request.files['image']
        path="static/uploads/"+str(uuid.uuid4())+image.filename
        image.save(path)
        
    
        q="insert into pest values (null,'%s','%s','%s')"%(pest,details,path)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_pest"))

    data={}
    q="select * from pest"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from pest where pest_id='%s'"%(pid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            pest=request.form['pest']
            details=request.form['details']
            if request.files['image']:
                image=request.files['image']
                path="static/uploads/"+str(uuid.uuid4())+image.filename
                image.save(path)

                q="update pest set pest='%s', details='%s', image='%s' where pest_id='%s' "%(pest,details,path,pid)
            else:
                q="update pest set pest='%s', details='%s' where pest_id='%s' "%(pest,details,pid)

            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_pest"))
    if action == "delete":
        q="delete from pest where pest_id='%s' "%(pid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_pest"))
    return render_template('admin_manage_pest.html',data=data) 




@admin.route('/admin_manage_crops',methods=['get','post'])
def admin_manage_crops():
    data={}
    if 'btn' in request.form:
        crop=request.form['crop']
      
        
    
        q="insert into crops values (null,'%s')"%(crop)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_crops"))

    data={}
    q="select * from crops"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from crops where crop_id='%s'"%(cid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            crop=request.form['crop']
          
        
            q="update crops set crop='%s' where crop_id='%s' "%(crop,cid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_crops"))
    if action == "delete":
        q="delete from crops where crop_id='%s' "%(cid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_crops"))
    return render_template('admin_manage_crops.html',data=data) 



@admin.route('/admin_manage_harmfullpest',methods=['get','post'])
def admin_manage_harmfullpest():
    data={}
    q='select * from pest'
    data['pest']=select(q)    
    q='select * from crops'
    data['crop']=select(q)    
    if 'btn' in request.form:
        c_id=request.form['c_id']
        p_id=request.form['p_id']
        details=request.form['details']  
    
        q="insert into harmfull values (null,'%s','%s','%s')"%(c_id,p_id,details)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_harmfullpest"))


    q="select *,harmfull.details as details from harmfull, crops, pest where harmfull.crop_id=crops.crop_id and harmfull.pest_id=pest.pest_id "
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        hid=request.args['hid'] 
    else:
        action=None

    
    
    if action == "delete":
        q="delete from harmfull where harmfull_id='%s' "%(hid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_harmfullpest"))
    return render_template('admin_manage_harmfullpest.html',data=data) 



@admin.route('/admin_manage_pesticide',methods=['get','post'])
def admin_manage_pesticide():
    data={}
    q="SELECT * FROM pest INNER JOIN harmfull USING(pest_id) GROUP BY pest"
    data['harm']=select(q)    
    
    if 'btn' in request.form:
        hm_id=request.form['hm_id']
        pest=request.form['pest']
        amount=request.form['amount']
        img=request.files['img']
        path='static/'+str(uuid.uuid4())+img.filename
        img.save(path)
        
        print("..................",hm_id)
        
    
        q="insert into pesticide values (null,'%s','%s','%s','%s')"%(hm_id,pest,amount,path)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_pesticide"))


    q="select *,pesticide.image as img from harmfull, pesticide, pest where harmfull.harmfull_id=pesticide.harmfull_id and harmfull.pest_id=pest.pest_id "
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid'] 
    else:
        action=None

    
    
    if action == "delete":
        q="delete from pesticide where pesticide_id='%s' "%(pid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_pesticide"))

    if action == "update":
        q="select * from pesticide where pesticide_id='%s'"%(pid)
        val=select(q)
        data['raw']=val

    if 'update' in request.form:
        pest=request.form['pest']
        amount=request.form['amount']
        if request.files['img']:
            image=request.files['image']
            path="static/uploads/"+str(uuid.uuid4())+image.filename
            image.save(path)

            q="update pesticide set pesticide='%s', amount='%s', image='%s' where pesticide_id='%s' "%(pest,amount,path,pid)
        else:
            q="update pesticide set pesticide='%s', amount='%s' where pesticide_id='%s' "%(pest,amount,pid)

        update(q)
        flash("Updated Successfully")
        return redirect(url_for("admin.admin_manage_pesticide"))
    return render_template('admin_manage_pesticide.html',data=data) 



import uuid
@admin.route('/admin_manage_trainingvideos',methods=['get','post'])
def admin_manage_trainingvideos():
    data={}
    if 'btn' in request.form:
        title=request.form['title']
        desc=request.form['desc']
        video=request.files['video']
        path="static/uploads/"+str(uuid.uuid4())+video.filename
        video.save(path)
        
    
        q="insert into traning values (null,'%s','%s','%s',curdate())"%(title,desc,path)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_trainingvideos"))

    data={}
    q="select * from traning"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        train_id=request.args['train_id'] 
    else:
        action=None

    
    if action == "update":
        q="select * from traning where traning_id='%s'"%(train_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
  
            title=request.form['title']
            desc=request.form['desc']
            if request.files['video']:
                video=request.files['video']
                path="static/uploads/"+str(uuid.uuid4())+video.filename
                video.save(path)
                q="update traning set title='%s', description='%s', video_link='%s' where traning_id='%s' "%(title,desc,path,train_id)
                update(q)
            else:
                q="update traning set title='%s', description='%s' where traning_id='%s' "%(title,desc,train_id)
                update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_trainingvideos"))
    if action == "delete":
        q="delete from traning where traning_id='%s' "%(train_id)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_trainingvideos"))
    return render_template('admin_manage_trainingvideos.html',data=data) 


@admin.route('/admin_complaints',methods=['get','post'])
def admin_complaints():
    data={}
    q="select * from complaint inner join customer using (customer_id)"
    res=select(q)
    data['res']=res

    for i in range(1,len(res)+1):
        if 'btn'+str(i) in request.form:
          
            comp_id=request.form['cid'+str(i)]
            reply=request.form['reply'+str(i)]
            print("sssssssssssssssssssssssssssss",comp_id,reply)
            q="update complaint set complaint_reply='%s' where complaint_id='%s'"%(reply,comp_id)
            update(q)
            return redirect(url_for("admin.admin_complaints"))
    return render_template('admin_complaints.html',data=data)



@admin.route('/admin_view_bookings')
def admin_view_bookings():
    data={}
    q="""
      
    SELECT fname,pordermaster.pordermaster_id,lname,phone,place,pesticide AS product,pquantity,p_amount AS total FROM `pordermaster`,`porderdetails`,`pesticide`,`customer` WHERE `pordermaster`.`pordermaster_id`=`porderdetails`.`pordermaster_id` AND `porderdetails`.`pesticide_id`=`pesticide`.`pesticide_id` AND `pordermaster`.`customer_id`=`customer`.`login_id`
    UNION
    SELECT fname,pordermaster.pordermaster_id,lname,phone,place,pesticide AS product,pquantity,p_amount AS total FROM `pordermaster`,`porderdetails`,`pesticide`,`farmer` WHERE `pordermaster`.`pordermaster_id`=`porderdetails`.`pordermaster_id` AND `porderdetails`.`pesticide_id`=`pesticide`.`pesticide_id` AND `pordermaster`.`customer_id`=`farmer`.`login_id`

    """
    data['res']=select(q)
    return render_template('admin_view_bookings.html',data=data)


@admin.route('/admin_view_payment')
def admin_view_payment():
    data={}
    pmid=request.args['pmid']
    q="select * from payment where ordermaster_id='%s' and type='pesticide'"%(pmid)
    data['res']=select(q)
    return render_template('admin_view_payment.html',data=data)