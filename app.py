from flask import *
import pymysql


#start
app = Flask(__name__)

@app.route('/')
def main():
    return ('this is my homepage')

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


        
app.run(debug=True)