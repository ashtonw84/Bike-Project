



# from email import message
# from glob import glob
# import os
# import psycopg2
# from flask import Flask, redirect, url_for, render_template, request
# import rsa
# import re
# from localStoragePy import localStoragePy


# publicKey = rsa.PublicKey(8864864214230065995202763740218556574899068353919685421281676565235580684818448523110255698019682719811712782298650452722634769219182668510002703110424729, 65537)
# privateKey = rsa.PrivateKey(8864864214230065995202763740218556574899068353919685421281676565235580684818448523110255698019682719811712782298650452722634769219182668510002703110424729, 65537, 5138447926669999344275181789880869236725297292044204186698328110230392584069310658951796951190624670637471368763343696551567043315572191461868294028892689, 7179446398685968393772375702460218939053042696689799791218826447466322590177261883, 1234755957764734388111524350388830462126863373341709945592578123205576763)
# global encPasw
# app = Flask(__name__)

# def get_db_connection():

#     conn = psycopg2.connect(
#         "dbname=postgres user=ashton_w84 host=localhost "  #REMEMBER TO CHANGE THE PASSWORD
#     )

#     return conn

# @app.route('/')
# def start():
#     return render_template('SignUp.html')

# @app.route('/', methods=['POST', 'GET'])
# def SignUp():
#     if request.method == 'POST':
#         name = request.form['fullname']
#         email = request.form['fullemail']
#         user = request.form['usrnme']
#         pasww = request.form['pswd']
#         pasw = ''
#         if re.match('(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$',pasww):
#             pasw = pasww
#         else:
#             exists = 'WEAK PASSWORD'
#             return render_template('SignUp.html', exists = exists)
#         conn = get_db_connection()
#         cur = conn.cursor()
#         # RUN CODE BELOW THE FIRST TIME ONLY
#         # cur.execute('CREATE TABLE lab4 (name varchar(500),email varchar(500),username varchar(500),password BYTEA)')
#         cur.execute('SELECT * FROM lab4;')
#         books = cur.fetchall()
#         if name == '' or email == '' or user == '' or pasw == '':
#             exists = 'Fields can not be left empty!'
#             return render_template('SignUp.html', exists = exists)
#         for i in range(0,len(books)):
#             if books[i][0] == name and books[i][1] == email:
#                 exists = 'User already exists, Try login in instead!'
#                 return render_template('SignUp.html', exists = exists)
#         x = bytes(pasw, 'utf-8')
#         encPasw = rsa.encrypt(x,publicKey)
#         cur.execute('INSERT INTO lab4(name, email, username, password) VALUES(%s, %s, %s, %s)', (name,email,user,encPasw))
#         conn.commit()
#         cur.execute('SELECT * FROM lab4;')
#         books = cur.fetchall()
#         cur.close()
#         conn.close()
#         return render_template('Login.html')

# @app.route('/Login')
# def Log():
#     return render_template('Login.html')


# @app.route('/Login', methods=['POST', 'GET'])
# def Login():
#     message = ''
#     if request.method == 'POST':
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute('SELECT * FROM lab4')
#         books = cur.fetchall()
#         user2 = request.form['fullname1']
#         pasw2 = request.form['pswrd1']
#         for i in range(0,len(books)):
#             if books[i][2] == user2:
#                 x = books[i][3]
#                 info = rsa.decrypt(x,privateKey).decode()
#                 if pasw2 == info:
#                     cur.close()
#                     conn.close()
#                     return redirect("http://127.0.0.1:5000/bike")
#                 else:
#                     message = 'WRONG USERNAME OR PASSWORD'
#                     cur.close()
#                     conn.close()
#                     return render_template('Login.html', message = message)
#         message = 'WRONG USERNAME OR PASSWORD'
#         cur.close()
#         conn.close()
#         return render_template('Login.html', books = books, message = message)

# @app.route('/bike')
# def bike1():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM bike')
#     books = cur.fetchall()
#     conn.commit()
#     bike = books[0][0]
#     bikedesc = books[0][1]
#     bikeimg = books[0][2]
#     bikeprice = books[0][3]
#     bike1 = books[1][0]
#     bike1desc = books[1][1]
#     bike1img = books[1][2]
#     bike1price = books[1][3]
#     bike2 = books[2][0]
#     bike2desc = books[2][1]
#     bike2img = books[2][2]
#     bike2price = books[2][3]
#     bike3 = books[3][0]
#     bike3desc = books[3][1]
#     bike3img = books[3][2]
#     bike3price = books[3][3]
#     bike4 = books[4][0]
#     bike4desc = books[4][1]
#     bike4img = books[4][2]
#     bike4price = books[4][3]
#     bike5 = books[5][0]
#     bike5desc = books[5][1]
#     bike5img = books[5][2]
#     bike5price = books[5][3]
#     bike6 = books[6][0]
#     bike6desc = books[6][1]
#     bike6img = books[6][2]
#     bike6price = books[6][3]
#     bike7 = books[7][0]
#     bike7desc = books[7][1]
#     bike7img = books[7][2]
#     bike7price = books[7][3]
#     bike8 = books[8][0]
#     bike8desc = books[8][1]
#     bike8img = books[8][2]
#     bike8price = books[8][3]
#     bike9 = books[9][0]
#     bike9desc = books[9][1]
#     bike9img = books[9][2]
#     bike9price = books[9][3]
#     print(books[0][0])
#     cur.close()
#     conn.close()
#     return render_template('bike.html',bike=bike,bikedesc=bikedesc,bikeimg=bikeimg,bikeprice=bikeprice,bike1=bike1,bike1desc=bike1desc,bike1img=bike1img,bike1price=bike1price,bike2=bike2,bike2desc=bike2desc,bike2img=bike2img,bike2price=bike2price,bike3=bike3,bike3desc=bike3desc,bike3img=bike3img,bike3price=bike3price,bike4=bike4,bike4desc=bike4desc,bike4img=bike4img,bike4price=bike4price,bike5=bike5,bike5desc=bike5desc,bike5img=bike5img,bike5price=bike5price,bike6=bike6,bike6desc=bike6desc,bike6img=bike6img,bike6price=bike6price,bike7=bike7,bike7desc=bike7desc,bike7img=bike7img,bike7price=bike7price,bike8=bike8,bike8desc=bike8desc,bike8img=bike8img,bike8price=bike8price,bike9=bike9,bike9desc=bike9desc,bike9img=bike9img,bike9price=bike9price,)
    

# @app.route('/bike1')
# def bikeDec1():
#     return render_template('bike1.html')

# @app.route('/bike2')
# def bikeDec2():
#     return render_template('bike2.html')
# @app.route('/bike3')
# def bikeDec3():
#     return render_template('bike3.html')
# @app.route('/bike4')
# def bikeDec4():
#     return render_template('bike4.html')
# @app.route('/bike5')
# def bikeDec5():
#     return render_template('bike5.html')
# @app.route('/bike6')
# def bikeDec6():
#     return render_template('bike6.html')
# @app.route('/bike7')
# def bikeDec7():
#     return render_template('bike7.html')
# @app.route('/bike8')
# def bikeDec8():
#     return render_template('bike8.html')
# @app.route('/bike9')
# def bikeDec9():
#     return render_template('bike9.html')
# @app.route('/bike10')
# def bikeDec10():
#     return render_template('bike10.html')
    

# @app.route('/Customize' , methods=['GET', 'POST']) 
# def custom():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM customize')
#     books = cur.fetchall()
#     conn.commit()
#     Cbike = books[0][0]
#     Cbikedesc = books[0][1]
#     Cbikeimg = books[0][2]
#     Cbikeprice = books[0][3]
#     Cbike1 = books[1][0]
#     Cbike1desc = books[1][1]
#     Cbike1img = books[1][2]
#     Cbike1price = books[1][3]
#     Cbike2 = books[2][0]
#     Cbike2desc = books[2][1]
#     Cbike2img = books[2][2]
#     Cbike2price = books[2][3]
#     Cbike3 = books[3][0]
#     Cbike3desc = books[3][1]
#     Cbike3img = books[3][2]
#     Cbike3price = books[3][3]
#     Cbike4 = books[4][0]
#     Cbike4desc = books[4][1]
#     Cbike4img = books[4][2]
#     Cbike4price = books[4][3]
#     Cbike5 = books[5][0]
#     Cbike5desc = books[5][1]
#     Cbike5img = books[5][2]
#     Cbike5price = books[5][3]
#     Cbike6 = books[6][0]
#     Cbike6desc = books[6][1]
#     Cbike6img = books[6][2]
#     Cbike6price = books[6][3]
#     Cbike7 = books[7][0]
#     Cbike7desc = books[7][1]
#     Cbike7img = books[7][2]
#     Cbike7price = books[7][3]
#     Cbike8 = books[8][0]
#     Cbike8desc = books[8][1]
#     Cbike8img = books[8][2]
#     Cbike8price = books[8][3]
#     Cbike9 = books[9][0]
#     Cbike9desc = books[9][1]
#     Cbike9img = books[9][2]
#     Cbike9price = books[9][3]
#     Cbike10 = books[10][0]
#     Cbike10desc = books[10][1]
#     Cbike10img = books[10][2]
#     Cbike10price = books[10][3]
#     Cbike11 = books[11][0]
#     Cbike11desc = books[11][1]
#     Cbike11img = books[11][2]
#     Cbike11price = books[11][3]
#     Cbike12 = books[12][0]
#     Cbike12desc = books[12][1]
#     Cbike12img = books[12][2]
#     Cbike12price = books[12][3]
#     Cbike13 = books[13][0]
#     Cbike13desc = books[13][1]
#     Cbike13img = books[13][2]
#     Cbike13price = books[13][3]
#     Cbike14 = books[14][0]
#     Cbike14desc = books[14][1]
#     Cbike14img = books[14][2]
#     Cbike14price = books[14][3]
#     Cbike15 = books[15][0]
#     Cbike15desc = books[15][1]
#     Cbike15img = books[15][2]
#     Cbike15price = books[15][3]
#     Cbike16 = books[16][0]
#     Cbike16desc = books[16][1]
#     Cbike16img = books[16][2]
#     Cbike16price = books[16][3]
#     Cbike17 = books[17][0]
#     Cbike17desc = books[17][1]
#     Cbike17img = books[17][2]
#     Cbike17price = books[17][3]
#     cur.close()
#     conn.close()
#     return render_template('Customize.html',Cbike=Cbike,Cbikedesc=Cbikedesc,Cbikeimg=Cbikeimg,Cbikeprice=Cbikeprice,Cbike1=Cbike1,Cbike1desc=Cbike1desc,Cbike1img=Cbike1img,Cbike1price=Cbike1price,Cbike2=Cbike2,Cbike2desc=Cbike2desc,Cbike2img=Cbike2img,Cbike2price=Cbike2price,Cbike3=Cbike3,Cbike3desc=Cbike3desc,Cbike3img=Cbike3img,Cbike3price=Cbike3price,Cbike4=Cbike4,Cbike4desc=Cbike4desc,Cbike4img=Cbike4img,Cbike4price=Cbike4price,Cbike5=Cbike5,Cbike5desc=Cbike5desc,Cbike5img=Cbike5img,Cbike5price=Cbike5price,Cbike6=Cbike6,Cbike6desc=Cbike6desc,Cbike6img=Cbike6img,Cbike6price=Cbike6price,Cbike7=Cbike7,Cbike7desc=Cbike7desc,Cbike7img=Cbike7img,Cbike7price=Cbike7price,Cbike8=Cbike8,Cbike8desc=Cbike8desc,Cbike8img=Cbike8img,Cbike8price=Cbike8price,Cbike9=Cbike9,Cbike9desc=Cbike9desc,Cbike9img=Cbike9img,Cbike9price=Cbike9price,Cbike10=Cbike10,Cbike10desc=Cbike10desc,Cbike10img=Cbike10img,Cbike10price=Cbike10price,Cbike11=Cbike11,Cbike11desc=Cbike11desc,Cbike11img=Cbike11img,Cbike11price=Cbike11price,Cbike12=Cbike12,Cbike12desc=Cbike12desc,Cbike12img=Cbike12img,Cbike12price=Cbike12price,Cbike13=Cbike13,Cbike13desc=Cbike13desc,Cbike13img=Cbike13img,Cbike13price=Cbike13price,Cbike14=Cbike14,Cbike14desc=Cbike14desc,Cbike14img=Cbike14img,Cbike14price=Cbike14price,Cbike15=Cbike15,Cbike15desc=Cbike15desc,Cbike15img=Cbike15img,Cbike15price=Cbike15price,Cbike16=Cbike16,Cbike16desc=Cbike16desc,Cbike16img=Cbike16img,Cbike16price=Cbike16price,Cbike17=Cbike17,Cbike17desc=Cbike17desc,Cbike17img=Cbike17img,Cbike17price=Cbike17price)

# @app.route('/cart', methods=['GET', 'POST'])
# def cartPage():
#     item = request.form.to_dict()
#     print("item: ", list(item.keys())[0])
#     item = list(item.keys())[0]
#     cart = item
#     return render_template('cart.html', cart = cart)


# if __name__ == '__main__':
#     app.run(debug = True)




import psycopg2
from flask import Flask, redirect, url_for, render_template, request
import rsa
import re

bikes = ''' 
                <div class="shop-item">
                    <div class="tooltip shop-item-title">{{bike}}
                        <span class= "tooltiptext">{{bikedesc}}</span></div>
                    <img class="shop-item-image" src={{bikeimg}}>
                    <div class="shop-item-details">
                        <span class="shop-item-price">${{bikeprice}}</span>
                        <input class="btn btn-primary shop-item-button" type="submit" name="{{bike}}" onclick="counter()" value="Add to Cart">
                    </div>
                </div>
''' 
cbikes = ''' 
                <div class="shop-item">
                    <div class="tooltip shop-item-title">{{Cbike}}
                        <span class= "tooltiptext">{{Cbikedesc}}</span></div>
                    <img class="shop-item-image" style="width: 250px;" src="{{Cbikeimg}}">
                    <div class="shop-item-details">
                        <span class="shop-item-price">${{Cbikeprice}}</span>
                        <input class="btn btn-primary shop-item-button" type="submit" name="{{Cbike}}" onclick="counter()" value="Add to Cart">
                    </div>
                </div>
''' 

result = re.sub(r'{{bike}}', '{{bike1}}', bikes)
result = re.sub(r'{{bikedesc}}', 'Bike Description', result)
result = re.sub(r'{{bikeimg}}', 'BikeImage', result)
result = re.sub(r'{{bikeprice}}', '2.99', result)
#####
result1 = re.sub(r'{{Cbike}}', 'Custom Title', cbikes)
result1 = re.sub(r'{{Cbikedesc}}', 'Customize Description', result1)
result1 = re.sub(r'{{Cbikeimg}}', 'CustomImage', result1)
result1 = re.sub(r'{{Cbikeprice}}', '9.99', result1)

publicKey = rsa.PublicKey(8864864214230065995202763740218556574899068353919685421281676565235580684818448523110255698019682719811712782298650452722634769219182668510002703110424729, 65537)
privateKey = rsa.PrivateKey(8864864214230065995202763740218556574899068353919685421281676565235580684818448523110255698019682719811712782298650452722634769219182668510002703110424729, 65537, 5138447926669999344275181789880869236725297292044204186698328110230392584069310658951796951190624670637471368763343696551567043315572191461868294028892689, 7179446398685968393772375702460218939053042696689799791218826447466322590177261883, 1234755957764734388111524350388830462126863373341709945592578123205576763)
global encPasw
app = Flask(__name__)
items = []
quantity = []

def get_db_connection():

    conn = psycopg2.connect(
        "dbname=postgres user=ashton_w84 host=localhost."  #REMEMBER TO CHANGE THE PASSWORD
    )
    return conn

@app.route('/')
def start():
    return render_template('SignUp.html')

@app.route('/', methods=['POST', 'GET'])
def SignUp():
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['fullemail']
        user = request.form['usrnme']
        pasww = request.form['pswd']
        pasw = ''
        if re.match('(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$',pasww):
            pasw = pasww
        else:
            exists = 'WEAK PASSWORD'
            return render_template('SignUp.html', exists = exists)
        conn = get_db_connection()
        cur = conn.cursor()
        # RUN CODE BELOW THE FIRST TIME ONLY
        # cur.execute('CREATE TABLE lab4 (name varchar(500),email varchar(500),username varchar(500),password BYTEA)')
        cur.execute('SELECT * FROM lab4;')
        books = cur.fetchall()
        if name == '' or email == '' or user == '' or pasw == '':
            exists = 'Fields can not be left empty!'
            return render_template('SignUp.html', exists = exists)
        for i in range(0,len(books)):
            if books[i][0] == name and books[i][1] == email:
                exists = 'User already exists, Try login in instead!'
                return render_template('SignUp.html', exists = exists)
        x = bytes(pasw, 'utf-8')
        encPasw = rsa.encrypt(x,publicKey)
        cur.execute('INSERT INTO lab4(name, email, username, password) VALUES(%s, %s, %s, %s)', (name,email,user,encPasw))
        conn.commit()
        cur.execute('SELECT * FROM lab4;')
        books = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('Login.html')

@app.route('/Login')
def Log():
    return render_template('Login.html')


@app.route('/Login', methods=['POST', 'GET'])
def Login():
    message = ''
    if request.method == 'POST':
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM lab4')
        books = cur.fetchall()
        user2 = request.form['fullname1']
        pasw2 = request.form['pswrd1']
        for i in range(0,len(books)):
            if books[i][2] == user2:
                x = books[i][3]
                info = rsa.decrypt(x,privateKey).decode()
                if pasw2 == info:
                    cur.close()
                    conn.close()
                    return redirect("http://127.0.0.1:5000/bike")
                else:
                    message = 'WRONG USERNAME OR PASSWORD'
                    cur.close()
                    conn.close()
                    return render_template('Login.html', message = message)
        message = 'WRONG USERNAME OR PASSWORD'
        cur.close()
        conn.close()
        return render_template('Login.html', books = books, message = message)

@app.route('/bike', methods=['POST', 'GET'])
def bike():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
        
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bike')
    books = cur.fetchall()
    conn.commit()
    bike = books[0][0]
    bikedesc = books[0][1]
    bikeimg = books[0][2]
    bikeprice = books[0][3]
    bike1 = books[1][0]
    bike1desc = books[1][1]
    bike1img = books[1][2]
    bike1price = books[1][3]
    bike2 = books[2][0]
    bike2desc = books[2][1]
    bike2img = books[2][2]
    bike2price = books[2][3]
    bike3 = books[3][0]
    bike3desc = books[3][1]
    bike3img = books[3][2]
    bike3price = books[3][3]
    bike4 = books[4][0]
    bike4desc = books[4][1]
    bike4img = books[4][2]
    bike4price = books[4][3]
    bike5 = books[5][0]
    bike5desc = books[5][1]
    bike5img = books[5][2]
    bike5price = books[5][3]
    bike6 = books[6][0]
    bike6desc = books[6][1]
    bike6img = books[6][2]
    bike6price = books[6][3]
    bike7 = books[7][0]
    bike7desc = books[7][1]
    bike7img = books[7][2]
    bike7price = books[7][3]
    bike8 = books[8][0]
    bike8desc = books[8][1]
    bike8img = books[8][2]
    bike8price = books[8][3]
    bike9 = books[9][0]
    bike9desc = books[9][1]
    bike9img = books[9][2]
    bike9price = books[9][3]
    cur.close()
    conn.close()
    return render_template('bike.html',quantity = len(quantity) ,bike=bike,bikedesc=bikedesc,bikeimg=bikeimg,bikeprice=bikeprice,bike1=bike1,bike1desc=bike1desc,bike1img=bike1img,bike1price=bike1price,bike2=bike2,bike2desc=bike2desc,bike2img=bike2img,bike2price=bike2price,bike3=bike3,bike3desc=bike3desc,bike3img=bike3img,bike3price=bike3price,bike4=bike4,bike4desc=bike4desc,bike4img=bike4img,bike4price=bike4price,bike5=bike5,bike5desc=bike5desc,bike5img=bike5img,bike5price=bike5price,bike6=bike6,bike6desc=bike6desc,bike6img=bike6img,bike6price=bike6price,bike7=bike7,bike7desc=bike7desc,bike7img=bike7img,bike7price=bike7price,bike8=bike8,bike8desc=bike8desc,bike8img=bike8img,bike8price=bike8price,bike9=bike9,bike9desc=bike9desc,bike9img=bike9img,bike9price=bike9price,)
    

@app.route('/bike1', methods=['POST', 'GET'])
def bikeDec1():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike1.html',quantity = len(quantity))

@app.route('/bike2', methods=['POST', 'GET'])
def bikeDec2():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike2.html',quantity = len(quantity))
@app.route('/bike3', methods=['POST', 'GET'])
def bikeDec3():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike3.html',quantity = len(quantity))
@app.route('/bike4', methods=['POST', 'GET'])
def bikeDec4():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike4.html',quantity = len(quantity))
@app.route('/bike5', methods=['POST', 'GET'])
def bikeDec5():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike5.html',quantity = len(quantity))
@app.route('/bike6', methods=['POST', 'GET'])
def bikeDec6():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike6.html',quantity = len(quantity))
@app.route('/bike7', methods=['POST', 'GET'])
def bikeDec7():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike7.html',quantity = len(quantity))
@app.route('/bike8', methods=['POST', 'GET'])
def bikeDec8():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike8.html',quantity = len(quantity))
@app.route('/bike9', methods=['POST', 'GET'])
def bikeDec9():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike9.html',quantity = len(quantity))
@app.route('/bike10', methods=['POST', 'GET'])
def bikeDec10():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)
    return render_template('bike10.html',quantity = len(quantity))
    

@app.route('/Customize', methods=['POST', 'GET'])
def custom():
    if request.method == 'POST':
        item = str(request.form.values)
        item = item[55:]
        item = item[:-4]
        item = item.split(',')
        x = str(item[0])
        x = x[1:]
        x = x[:-1]
        items.append(x)
        quantity.append(1)

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM customize')
    books = cur.fetchall()
    conn.commit()
    Cbike = books[0][0]
    Cbikedesc = books[0][1]
    Cbikeimg = books[0][2]
    Cbikeprice = books[0][3]
    Cbike1 = books[1][0]
    Cbike1desc = books[1][1]
    Cbike1img = books[1][2]
    Cbike1price = books[1][3]
    Cbike2 = books[2][0]
    Cbike2desc = books[2][1]
    Cbike2img = books[2][2]
    Cbike2price = books[2][3]
    Cbike3 = books[3][0]
    Cbike3desc = books[3][1]
    Cbike3img = books[3][2]
    Cbike3price = books[3][3]
    Cbike4 = books[4][0]
    Cbike4desc = books[4][1]
    Cbike4img = books[4][2]
    Cbike4price = books[4][3]
    Cbike5 = books[5][0]
    Cbike5desc = books[5][1]
    Cbike5img = books[5][2]
    Cbike5price = books[5][3]
    Cbike6 = books[6][0]
    Cbike6desc = books[6][1]
    Cbike6img = books[6][2]
    Cbike6price = books[6][3]
    Cbike7 = books[7][0]
    Cbike7desc = books[7][1]
    Cbike7img = books[7][2]
    Cbike7price = books[7][3]
    Cbike8 = books[8][0]
    Cbike8desc = books[8][1]
    Cbike8img = books[8][2]
    Cbike8price = books[8][3]
    Cbike9 = books[9][0]
    Cbike9desc = books[9][1]
    Cbike9img = books[9][2]
    Cbike9price = books[9][3]
    Cbike10 = books[10][0]
    Cbike10desc = books[10][1]
    Cbike10img = books[10][2]
    Cbike10price = books[10][3]
    Cbike11 = books[11][0]
    Cbike11desc = books[11][1]
    Cbike11img = books[11][2]
    Cbike11price = books[11][3]
    Cbike12 = books[12][0]
    Cbike12desc = books[12][1]
    Cbike12img = books[12][2]
    Cbike12price = books[12][3]
    Cbike13 = books[13][0]
    Cbike13desc = books[13][1]
    Cbike13img = books[13][2]
    Cbike13price = books[13][3]
    Cbike14 = books[14][0]
    Cbike14desc = books[14][1]
    Cbike14img = books[14][2]
    Cbike14price = books[14][3]
    Cbike15 = books[15][0]
    Cbike15desc = books[15][1]
    Cbike15img = books[15][2]
    Cbike15price = books[15][3]
    Cbike16 = books[16][0]
    Cbike16desc = books[16][1]
    Cbike16img = books[16][2]
    Cbike16price = books[16][3]
    Cbike17 = books[17][0]
    Cbike17desc = books[17][1]
    Cbike17img = books[17][2]
    Cbike17price = books[17][3]
    cur.close()
    conn.close()
    return render_template('Customize.html',quantity = len(quantity),Cbike=Cbike,Cbikedesc=Cbikedesc,Cbikeimg=Cbikeimg,Cbikeprice=Cbikeprice,Cbike1=Cbike1,Cbike1desc=Cbike1desc,Cbike1img=Cbike1img,Cbike1price=Cbike1price,Cbike2=Cbike2,Cbike2desc=Cbike2desc,Cbike2img=Cbike2img,Cbike2price=Cbike2price,Cbike3=Cbike3,Cbike3desc=Cbike3desc,Cbike3img=Cbike3img,Cbike3price=Cbike3price,Cbike4=Cbike4,Cbike4desc=Cbike4desc,Cbike4img=Cbike4img,Cbike4price=Cbike4price,Cbike5=Cbike5,Cbike5desc=Cbike5desc,Cbike5img=Cbike5img,Cbike5price=Cbike5price,Cbike6=Cbike6,Cbike6desc=Cbike6desc,Cbike6img=Cbike6img,Cbike6price=Cbike6price,Cbike7=Cbike7,Cbike7desc=Cbike7desc,Cbike7img=Cbike7img,Cbike7price=Cbike7price,Cbike8=Cbike8,Cbike8desc=Cbike8desc,Cbike8img=Cbike8img,Cbike8price=Cbike8price,Cbike9=Cbike9,Cbike9desc=Cbike9desc,Cbike9img=Cbike9img,Cbike9price=Cbike9price,Cbike10=Cbike10,Cbike10desc=Cbike10desc,Cbike10img=Cbike10img,Cbike10price=Cbike10price,Cbike11=Cbike11,Cbike11desc=Cbike11desc,Cbike11img=Cbike11img,Cbike11price=Cbike11price,Cbike12=Cbike12,Cbike12desc=Cbike12desc,Cbike12img=Cbike12img,Cbike12price=Cbike12price,Cbike13=Cbike13,Cbike13desc=Cbike13desc,Cbike13img=Cbike13img,Cbike13price=Cbike13price,Cbike14=Cbike14,Cbike14desc=Cbike14desc,Cbike14img=Cbike14img,Cbike14price=Cbike14price,Cbike15=Cbike15,Cbike15desc=Cbike15desc,Cbike15img=Cbike15img,Cbike15price=Cbike15price,Cbike16=Cbike16,Cbike16desc=Cbike16desc,Cbike16img=Cbike16img,Cbike16price=Cbike16price,Cbike17=Cbike17,Cbike17desc=Cbike17desc,Cbike17img=Cbike17img,Cbike17price=Cbike17price)

@app.route('/cart', methods=['POST', 'GET'])
def cart():
    carts = ''' 
            <div class="cart-row">
                <span><img class="shop-item-image" src={{IMAGE}} style="width:50px;margin-right: 70px;margin-left: -120px;"></span>
                <span class="cart-item cart-header cart-column" style="margin-right: 80px;">{{NAME}}</span>
                <span style="margin-right: 10px;"></span>
                <span class="cart-price cart-header cart-column" style="margin-right: 80px;">${{PRICE}}</span>
                <span style="margin-right: 60px;"></span>
                <span class="cart-quantity cart-header cart-column" style="margin-right: 120px;">{{QUANTITY}}</span>
                <span class="cart-quantity cart-header cart-column" style="margin-right: -80px;">${{SUBTOTAL}}</span>
            </div>
    '''
    print(items)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM customize')
    customize = cur.fetchall()
    conn.commit()
    cur.execute('SELECT * FROM bike')
    bikes = cur.fetchall()
    conn.commit()
    total = 0.00
    htmlPass = []
    for i in range(0,len(items)):
        for x in bikes:
            if x[0] in items[i]:
                total = total + x[3]
                result2 = re.sub(r'{{IMAGE}}', x[2], carts)
                result2 = re.sub(r'{{PRICE}}', str(x[3]), result2)
                result2 = re.sub(r'{{NAME}}', x[0], result2)
                result2 = re.sub(r'{{QUANTITY}}', str(items.count(items[i])), result2)
                result2 = re.sub(r'{{SUBTOTAL}}', str(x[3]*items.count(items[i])), result2)
                htmlPass.append(result2)

        for y in customize:
            if y[0] in items[i]:
                total = total + y[3]
                result2 = re.sub(r'{{IMAGE}}', y[2], carts)
                result2 = re.sub(r'{{PRICE}}', str(y[3]), result2)
                result2 = re.sub(r'{{NAME}}', y[0], result2)
                result2 = re.sub(r'{{QUANTITY}}', str(items.count(items[i])), result2)
                result2 = re.sub(r'{{SUBTOTAL}}', str(y[3]*items.count(items[i])), result2)
                htmlPass.append(result2)
    
    return render_template('cart.html', total = total, htmlPass = htmlPass)

@app.route('/receipt')
def receipt():
    return render_template('receipt.html')


@app.route('/thankYou')
def thankYou():
    return render_template('thankYou.html')

if __name__ == '__main__':
    app.run(debug = True)




