@app.route('/login_two', methods=['GET', 'POST'])
def login_two():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = supabase_client.auth.sign_in_with_password({'email':email, 'password': password})
        return redirect(url_for('index'))
    return render_template('login_two.html')