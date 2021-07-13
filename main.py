from flask import Flask
from flask import render_template
from flask import redirect, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = 'Homer'
    return render_template('index.html', title='Welcome', username=name)

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

