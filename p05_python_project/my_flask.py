from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

app.run('0.0.0.0')

##For specific port use 
#app.run(host='0.0.0.0', port=5001)
