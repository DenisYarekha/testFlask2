from flask import Flask, render_template_string, session, request, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'key' 

USER = {
    "username": "admin",
    "password": "1234"
}

@app.route('/', methods = ['GET', 'POST'])
def login():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('generate_code'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USER['username'] and password == USER['password']:
            session['logged_in'] = True
            return redirect(url_for('generate_code'))
        else:
            return "ERROR", 401
    return ('''
        <h1>Login:</h1>
        <form action="/" method="post">
            Login: <input type="text" name="username">
            Password: <input type="password" name="password">
            <input type="submit" value="Enter">
        </form>
    ''')

@app.route('/code')
def generate_code():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    code = random.randint(1000, 9999)
    session.clear()
    return f"<h1>Code: {code}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
