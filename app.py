# from flask import Flask, redirect, render_template, request ,jsonify, session, url_for
# import supabase
# from flask_sqlalchemy import SQLAlchemy
# #extra
# supabase_url = 'https://scwujjreobpuxdlbaojp.supabase.co'
# supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNjd3VqanJlb2JwdXhkbGJhb2pwIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzg2NDUzNjQsImV4cCI6MTk5NDIyMTM2NH0.ialCpqxh-PJz1FRW4MSDXQvmnI_NWHsprqmfe5wZvCQ'
# supabase_client = supabase.create_client(supabase_url, supabase_key)
# #extra

# app = Flask(_name_)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/imaid"
# db = SQLAlchemy(app)


# @app.route('/')
# def signup():
#     return render_template('signup.html')
# @app.route('/login_two/')
# def login():
#     return render_template('login_two.html')
# @app.route('/index/')
# def about():
#     return render_template('index.html')

#---------------------------------------------------------------------------------------
# class Register_details(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), unique=False, nullable=False)
#     contact = db.Column(db.String(20), unique=True, nullable=False)
#     adderess = db.Column(db.String(50), unique=False, nullable=False)
#     aadhar = db.Column(db.String(12), unique=True, nullable=False)
#     file = db.Column(db.LargeBinary)


# @app.route("/login", methods=['GET', 'POST'])
# def index():
#     if (request.method == 'POST'):
#         '''Add entry to the database'''
#         name = request.form.get('name')
#         contact = request.form.get('contact')
#         adderess = request.form.get('adderess')
#         aadhar = request.form.get('aadhar')
#         file = request.files['file']
#         data = file.read()
#         entry = Register_details(
#             name=name, contact=contact, adderess=adderess, aadhar=aadhar, file=data)
#         db.session.add(entry)
#         db.session.commit()

#     return render_template('index.html')

#---------------------------------------------------------------------------
# if _name_ == "_main_":
#     app.run(debug=True)


#import jwt
import supabase

supabase_url = "https://scwujjreobpuxdlbaojp.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNjd3VqanJlb2JwdXhkbGJhb2pwIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzg2NDUzNjQsImV4cCI6MTk5NDIyMTM2NH0.ialCpqxh-PJz1FRW4MSDXQvmnI_NWHsprqmfe5wZvCQ"
supabase_client = supabase.create_client(supabase_url, supabase_key)

#new changes for registration form
#------------------------------------------------------------------------------------------------------
# data = {'name': 'Johny', 'password': '123343', 'email': 'johyyn@example.com'}
# table_name = 'maid'
# result = client.table(table_name).insert(data).execute()


# @app.route('/register', methods=['POST'])
# def register():
#     name = request.form.get('name')
#     address = request.form.get('address')
#     aadhar = request.form.get('aadhar')
#     contact = request.form.get('contact')
#     table_name='maidregisterdetails'
#     data = {'name': name, 'address': address, 'aadhar': aadhar,'contact':contact}
#     result = supabase_client.table(table_name).insert(data).execute()




# '''
# jo v colum cahhiye wo daalo select me to ho jayega.
# '''

# response = client.table(table_name).select('email').execute()
# '''
# response ka data hi print kr sakte h
# '''
# # Print the results
# print(response.data)
#------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def new():
    return render_template('signup.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = supabase_client.auth.sign_up({'email':email, 'password': password})
        return redirect(url_for('login_two'))
    return render_template('signup.html')

@app.route('/login_two', methods=['GET', 'POST'])
def login_two():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        res = supabase_client.auth.sign_in_with_password({'email':email, 'password': password})
        return redirect(url_for('index'))
    return render_template('login_two.html')
# @app.route('/login_two', methods=['GET', 'POST'])
# def login_two():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         res = supabase_client.auth.sign_in_with_password({'email':email, 'password': password})
#         return redirect(url_for('index'))
#     return render_template('login_two.html')

@app.route('/logout')
def logout():
    supabase_client.auth.sign_out()
    return redirect(url_for('login_two'))

@app.route('/dashboard')
def dashboard():
    user = supabase_client.auth.user()
    if user is None:
        return redirect(url_for('login_two'))
    return render_template('dashboard.html', user=user)
#----------------------------------------------------------------------------------------------------------
@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    address = request.form.get('address')
    aadhar = request.form.get('aadhar')
    contact = request.form.get('contact')
    table_name='maidregisterdetails'
    data = {'name': name, 'address': address, 'aadhar': aadhar,'contact':contact}
    result = supabase_client.table(table_name).insert(data).execute()
    return render_template('index.html')
#-------------------------------------------------------------------------------------------------------------
@app.route('/index')
def index():
    user = supabase_client.auth.get_user()
    if user is None:
        return redirect(url_for('login_two'))
    return render_template('index.html', user=user)

if __name__ =="__main__":
    app.run(debug=True)
 