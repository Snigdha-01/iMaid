
import supabase

supabase_url = "https://scwujjreobpuxdlbaojp.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNjd3VqanJlb2JwdXhkbGJhb2pwIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzg2NDUzNjQsImV4cCI6MTk5NDIyMTM2NH0.ialCpqxh-PJz1FRW4MSDXQvmnI_NWHsprqmfe5wZvCQ"
supabase_client = supabase.create_client(supabase_url, supabase_key)

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

@app.route('/index')
def index():
    user = supabase_client.auth.get_user()
    if user is None:
        return redirect(url_for('login_two'))
    return render_template('index.html', user=user)

if __name__ =="__main__":
    app.run(debug=True)
 