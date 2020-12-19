from flask import Flask, render_template, url_for, request, redirect

#initialising the app
app = Flask(__name__)

#declaring app routes
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/works')
def works():
    return render_template('works.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()