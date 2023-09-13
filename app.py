from flask import *
import pymysql


#start
app = Flask(__name__)

@app.route('/')
def main():
    return ('this is my homepage')

app.run(debug=True)