from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://JucCheol:wnscjf909@cluster0.505uedx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    comment_receive = request.form['comment_give']
    bucket_lis=list(db.buckets.find({},{'_id':False}))
    count=len(bucket_lis)
    doc={
        'num':count,
        'comment':comment_receive,
        'done': 0
    }
    db.buckets.insert_one(doc)
    return jsonify({'msg': '버킷리스트 저장'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.buckets.update_one({'num':int(num_receive)},{'$set':{'done':1}})
    return jsonify({'msg': '버킷완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    buckets_list=list(db.buckets.find({},{'_id':False}))
    return jsonify({'buckets': buckets_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)