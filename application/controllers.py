from flask import Flask, render_template, redirect, request, send_file
from flask import current_app as app
from .models import *
from jinja2 import FileSystemLoader, Environment
env=Environment(loader=FileSystemLoader(['template','other']))

@app.route('/', methods=['GET','POST'])
def homepage():
    return "Welcome to A-Z HouseHold Services"

@app.route('/userlogin', methods=['GET','POST'])
def userlogin():
    if request.method=="POST":
            
        u_email = request.form.get('u_email')  
        pwd = request.form.get("pwd")
        this_user = User.query.filter_by(email=u_email).first()
    
        
        if this_user is None:
            message = "User non exist"
            return render_template('login.html',error = message)
        
        if this_user.type == 'admin':
            this_user = User.query.filter_by(email=u_email).first()
            if this_user and this_user.password == pwd:
                return redirect('/adminDash')
            else:
                return "Admin login failed"
            
        

        elif this_user.type == 'user':
            this_user = User.query.filter_by(email=u_email).first()
            if this_user and this_user.password == pwd:
                return redirect('/cusdash')
            else:
                return "User login failed"
        
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        u_email = request.form.get("u_email")
        pwd = request.form.get("pwd")
        uname = request.form.get("u_name")
        add = request.form.get("u_address")
        pcode = request.form.get("u_pincode")

        this_user = User.query.filter_by(email = u_email).first()
        if this_user:
            message = "User already exist please login"
            return render_template('register.html',error = message)
        
        new_user = User(email = u_email, password = pwd,username=uname,address=add,pincode=pcode)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/userlogin')
    return render_template('register.html')

@app.route('/serviceSignup', methods=['GET','POST'])
def serviceSignup():
    if request.method == 'POST':
        proname = request.form.get("proname")
        propwd = request.form.get("propwd")
        pro_email = request.form.get("pro_email")
        options = request.form.get("options")
        exp = request.form.get("exp")
        proAdd = request.form.get("proAdd")
        proPin = request.form.get("proPin")
    
        this_pro = Professional.query.filter_by(email = pro_email).first()
        if this_pro:
            message = "Professional already exist please login"
            return render_template('serviceSignup.html', error = message)
    
        new_pro = Professional(email=pro_email, password = propwd, username = proname, service = options, exp = exp, add = proAdd, pin = proPin)
        db.session.add(new_pro)
        db.session.commit()
        return redirect('/userlogin')
    return render_template('serviceSignup.html')




@app.route('/adminDash', methods=['GET','POST'])
def adminDash():
   return render_template('adminDash.html')


@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('adminDash.html')

@app.route('/adminsummary', methods=['GET','POST'])
def adminsummary():
    return render_template('adminSummary.html')

@app.route('/professionalLogin', methods = ['GET', 'POST'])
def professionalLogin():
    if request.method=="POST":
        pro_email = request.form.get("pro_email")
        propwd = request.form.get("propwd")
        this_pro = Professional.query.filter_by(email=pro_email).first()

        if this_pro is None:
            message = "Professional non exist"
            return render_template('login.html',error = message)
    
        elif this_pro.type == 'professional':
            this_pro = Professional.query.filter_by(email=pro_email).first()
            if this_pro and this_pro.password == propwd:
                return redirect('/professionalDash')
            else:
                return "Professional login failed"
    

    return render_template('professionalLogin.html')

@app.route('/professionalDash', methods=['GET','POST'])
def professionalDash():
    return render_template('professionalDash.html')

@app.route('/professionalsummary', methods=['GET','POST'])
def professionalsummary():
    return render_template('professionalsummary.html')

@app.route('/professionalprofile', methods=['GET','POST'])
def professionalprofile():
    return render_template('professionalprofile.html')

@app.route('/cusdash', methods=['GET','POST'])
def cusdash():
    return render_template('cusDash.html')

@app.route('/review', methods=['GET','POST'])
def review():
    return render_template('review.html')

@app.route('/cussummary', methods=['GET','POST'])
def cussummary():
    return render_template('cussummary.html')


@app.route('/cleaner', methods=['GET','POST'])
def cleaner():
    return render_template('cleaner.html')

@app.route('/electrician', methods=['GET','POST'])
def electrician():
    return render_template('electrician.html')

@app.route('/mechanic', methods=['GET','POST'])
def mechanic():
    return render_template('mechanic.html')

@app.route('/plumber', methods=['GET','POST'])
def plumber():
    return render_template('plumber.html')

@app.route('/cook', methods=['GET','POST'])
def cook():
    return render_template('cook.html')

@app.route('/newservice', methods=['GET','POST'])
def newservice():
    if request.method == 'POST':
       service = request.form.get("service")
       description = request.form.get("description")
       base_price = request.form.get("base_price")
       if 'add' in request.form:
            new_service = Service(service_name=service, description = description, base_price = base_price)
            db.session.add(new_service)
            db.session.commit()
            return redirect('/home')
       return redirect('/home') 
    return render_template('newservice.html')