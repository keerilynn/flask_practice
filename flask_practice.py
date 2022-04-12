Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name="Treehouse"):
  name = request.args.get('name', name)
  return "Hello from {}".format(name)

app.run(debug=True, port=8000,host='0.0.0.0')
