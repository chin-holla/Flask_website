from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'siddhishi'

# Simple in-memory user database
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def home():
    username = session.get('username')
    return render_template('home.html',username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            # Successful login, store username in session
            session['username'] = username
            return redirect(url_for('home'))
        else:
            # Incorrect credentials
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html', error=None)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        new_username = request.form.get('new_username')
        new_password = request.form.get('new_password')

        # Simple validation 
        if new_username and new_password:
            # Add the new user to the database 
            users[new_username] = new_password

            # Log the user in automatically after signup
            session['username'] = new_username

            # Redirect to the home page after successful sign-up
            return redirect(url_for('home'))
        
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
