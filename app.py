from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  

client = MongoClient('52.78.73.206',username="test", password='test',authSource='admin', authMechanism='SCRAM-SHA-1')
db = client.dbsparta 



@app.route('/')
def home():
    return render_template('index.html')




@app.route('/rofan')
def rofan():
    return render_template('index2.html')

@app.route('/fantagy')
def fantagy():
    return render_template('index3.html')

@app.route('/marsharl')
def marsharl():
    return render_template('index4.html')


@app.route('/review/<int:review_num>')
def reviews(review_num):
    return render_template(f'review{review_num}.html')



@app.route('/reviews/<int:novel_no>', methods=['POST'])
def write_review(novel_no):
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    review = {
        'novel_no':novel_no,
        'author': author_receive,
        'review': review_receive
    }

    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/reviews/<int:novel_no>', methods=['GET'])
def read_reviews(novel_no):
    reviews = list(db.reviews.find({'novel_no': novel_no}, {'_id': 0}))
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)





    