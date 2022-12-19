from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://JucCheol:wnscjf909@cluster0.505uedx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta



@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])

def homework_post():
    say_receive = request.form['say_give']
    name_receive = request.form['name_give']

    doc={
        'name':name_receive,
        'comment':say_receive
    }
    db.pans.insert_one(doc)
    return jsonify({'msg':'응원 댓글 완료'})

@app.route("/homework", methods=["GET"])
def homework_get():
    pans_list = list(db.pans.find({},{'_id':False}))
    return jsonify({'pans': pans_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)