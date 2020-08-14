from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    title = 'Home' 
    return render_template('home.html', title=title)

@app.route('/about')
def about():
    title = 'About' 
    return render_template('about.html', title=title)

@app.route('/subscribe')
def subscribe():
    title = 'Subscribe Form' 
    return render_template('subscribe.html', title=title)

@app.route('/form',  methods=["POST"])
def form():
    title = 'Form'
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    return render_template('form.html', title=title, firstname=firstname, lastname=lastname, email=email)

@app.route('/subscribers')
def subscribers():
    title = 'Subscribers List' 
    names = ['Alan', 'Peter', 'Nadia', 'Vanessa', 'lia']
    return render_template('subscribers.html', names=names, title=title)

if __name__ == "__main__":
    app.run(debug=True)