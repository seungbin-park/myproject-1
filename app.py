 
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  

client = MongoClient('localhost', 27017) 
db = client.dbsparta 



@app.route('/')
def home():
    return render_template('')


@app.route('/reviews', methods=['POST'])
def write_review():
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']
    

    review = {
        'author': author_receive,
        'review': review_receive,
        
    }

    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 작성되었습니다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)