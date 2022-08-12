from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'Name': 'Mikee Berdin',
        'Company': 'Appcove',
        'Email': 'mikee@appcove.com',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'hello@appcove.com' and form.password.data == 'password':
            flash('You have been logged in!')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
