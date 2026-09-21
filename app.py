from flask import Flask, render_template, request
#import flask in order to use it

app = Flask(__name__)
#instance of flask; passing variable __name__ to instance "app"

@app.route('/')
#app : decorator
#/ : home url
def hello():
    return '<center><h2>Hello World</h2><br><a href="/register">Go to registration</a></center>'

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/success', methods=['POST'])
def success():
    return '<center><h2>Registration Successful</h2></center>'

if __name__ == '__main__':
    app.run(debug = True)