from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy                #database import

myapp=Flask(__name__)

myapp.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
db=SQLAlchemy()
db.init_app(myapp)

class Customer(db.Model):
    fname=db.Column(db.String(50))
    lname=db.Column(db.String(50))
    address=db.Column(db.String(500))
    contact=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(200))
    

@myapp.route("/")
def hello():
    return render_template("homepage.html")

@myapp.route("/c")
def hello1():
    return render_template("child.html")

@myapp.route("/f")
def hello2():
    return render_template("footer.html")

@myapp.route("/about")
def about():
    return render_template("about.html")

@myapp.route("/ply")
def ply():
    
    return render_template("ply2.html")

@myapp.route("/estimate")
def estimate1():
    
    return render_template("estimate1.html")

@myapp.route('/crt',methods=['GET','POST'])                         # Add details in DB
def new():
    print("hello")
    if request.method == 'POST':
        print("In the post method")
        if request.form['fname']=='' or request.form['lname']=='' or request.form['address']=='' or request.form['contact']==None or request.form['email']=='' :
            print("in the details error function")
            return "<h3>Please fill all the details.</h3>"
        else:
            fnm=request.form['fname']
            lnm=request.form['lname']
            ad=request.form['address']
            con=request.form['contact']
            eml=request.form['email']
            print(fnm,lnm,ad,con,eml,sep="\n")
            c1=Customer(fname=fnm,lname=lnm,address=ad,contact=con,email=eml)
            print(c1)
            db.session.add(c1)
            print("addes")
            db.session.commit()
            print("committed")
            #return redirect(url_for('blank'))
            print("Over")
            print()
            print()
            print()
            print()
            
            
            return render_template('homepage.html')
    return render_template("estimate1.html")

@myapp.route('/crt',methods=['GET','POST']) 
def budget():
    return render_template("estimate2.html")
    
        
@myapp.route("/but")
def but():
    
    return render_template("button.html")
 
    return render_template ('estimate1.html')
print("THE NAME IS:-  ",__name__)

if __name__ =='__main__':
    myapp.app_context().push()
    db.create_all()
    myapp.run(debug=True)