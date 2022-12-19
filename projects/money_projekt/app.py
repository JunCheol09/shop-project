from flask import Flask,redirect,url_for, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://JucCheol:wnscjf909@cluster0.505uedx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/newpage", methods=["GET"])
def newpage_get():
    return render_template('index2.html')

@app.route("/anotherpage", methods=["GET"])
def anotherpage_get():
    return render_template('index3.html')



@app.route("/account", methods=["GET"])
def account_get():
    account_list=list(db.account.find({},{'_id':False}))
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

@app.route("/money", methods=["POST"])
def money_post():
    money_receive = request.form['money_give']
    recent_money_receive = request.form['recent_money_give']
    num_receive = request.form['num_give']
    db.account.update_one({'num': int(num_receive) },{'$set':{'money':int(money_receive)+int(recent_money_receive)}})
    return jsonify({'msg': '버킷완료!'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)