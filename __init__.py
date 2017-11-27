
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def homepage():
                return  render_template("index.html")
#app.debug=True
app.run(host='0.0.0.0')
##