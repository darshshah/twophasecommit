

from flask import Flask, url_for
app = Flask (__name__)


@app.route('/user/<username>')
def profile(username): pass

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='asda')
    print url_for('profile', username='Darshs')

#if __name__ == '__main__':
 #   app.run(debug=True)

