from flask import *
from database import *


admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@admin.route('/adminviewfarmers')
def adminviewfarmers():
    data={}
    q="select * from farmer"
    data['res']=select(q)
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
    q="select * from item"
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
        
    
        q="insert into pest values (null,'%s','%s')"%(pest,details)
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


    q="select * from harmfull, crops, pest where harmfull.crop_id=crops.crop_id and harmfull.pest_id=pest.pest_id "
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
    q='select * from pest inner join harmfull using (pest_id) group by pest_id'
    data['harm']=select(q)    
    
    if 'btn' in request.form:
        hm_id=request.form['hm_id']
        pest=request.form['pest']
        
    
        q="insert into pesticide values (null,'%s','%s')"%(hm_id,pest)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_pesticide"))


    q="select * from harmfull, pesticide, pest where harmfull.harmfull_id=pesticide.harmfull_id and harmfull.pest_id=pest.pest_id "
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