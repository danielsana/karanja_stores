from flask import *
import pymysql


#start
app = Flask(__name__)

#sessions
# step 1: provide secret key to your application
# avoid session hijacking, cross-site scripting

app.secret_key ="12325thv4365426nkghghdhjhjhhvhvfhgfghfd@@#$"


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/vendor_register', methods=['POST','GET'])
def vendor_Register():
    if request.method =='POST':
        vendor_name = request.form['name']
        vendor_contact = request.form['contact']
        vendor_email = request.form['email']
        vendor_location = request.form['location']
        vendor_password = request.form['password']

        vendor_photo = request.files['photo']
        vendor_photo.save('static/images/'+vendor_photo.filename)

        vendor_desc = request.form['desc']

        connection = pymysql.connect(host='localhost',user='root',password='',database='karanja_eshop')

        cursor=connection.cursor()

        sql ="insert into vendors (vendor_name,vendor_contact,vendor_email,vendor_location,vendor_password,vendor_photo,vendor_desc) values(%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(sql,(vendor_name,vendor_contact,vendor_email,vendor_location,vendor_password,vendor_photo.filename,vendor_desc))

        connection.commit()

        return render_template('vendor_register.html', message='vendor successfuly registerd')
    else:
        return render_template('vendor_register.html',message='Please Register Here')

@app.route('/vendor_login', methods =['POST','GET'])
def vendor_login():
    if request.method =='POST':
        vendor_name =request.form['name']
        vendor_password = request.form['password']

        connection = pymysql.connect(host='localhost',user='root',password='',database='karanja_eshop')

        cursor = connection.cursor()

        sql = "select * from vendors where vendor_name = %s and vendor_password = %s"

        cursor.execute(sql,(vendor_name,vendor_password))

        count = cursor.rowcount

        if count ==0:
            return render_template('vendor_login',message='invalid credential')
        else:
            #session
            user_record =cursor.fetchone()
            session['key'] =user_record[1]
            session['vendor_id']= user_record[0]
            session['contact'] = user_record[2]
            session['location'] = user_record[4]
            session['image'] = user_record[6]
            session['desc'] = user_record[7]
        
app.run(debug=True)