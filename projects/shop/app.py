from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi
ca = certifi.where();
client = MongoClient('mongodb+srv://JucCheol:wnscjf909@cluster0.505uedx.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta


x='anotherpage'

@app.route('/')
def home():
    data = ''
    return render_template('index.html', redirect_url=data)


@app.route("/anotherpage2", methods=["GET"])
def anotherpage2_get():
    return render_template('index2.html')


@app.route(f'/{x}', methods=["GET"])
def x_get():
    data = ''
    return render_template('index3.html',redirect_url=data)



@app.route("/shop", methods=["GET"])
def shop_get():
    shop_list = list(db.shop.find({},{'_id':False}))
    
    return jsonify({'shops':shop_list})



@app.route("/account", methods=["GET"])
def account_get():
    account_list=list(db.account.find({},{'_id':False}))
    global x
    x = '정준철'
    return jsonify({'account': account_list})



@app.route("/account", methods=["POST"])
def account_post():
    account_receive = request.form['account_give']
    password_receive = request.form['password_give']
    name_receive=request.form['name_give']
    account_lis=list(db.account.find({},{'_id':False}))
    count=len(account_lis)
    doc={
        'identity':account_receive,
        'password':password_receive,
        'money':0,
        'name':name_receive,
        'num':count,
    }
    db.account.insert_one(doc)
    return jsonify({'accounts': account_lis})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

print(x)