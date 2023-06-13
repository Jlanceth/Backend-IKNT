from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)

    def __init__(self, title, content):
        self.title = title
        self.content = content

@app.route('/news', methods=['GET'])
def get_news():
    news = News.query.all()
    result = [{'title': news.title, 'content': news.content} for news in news]
    return jsonify(result)

@app.route('/news', methods=['POST'])
def add_news():
    data = request.get_json()
    title = data['title']
    content = data['content']
    news = News(title, content)
    db.session.add(news)
    db.session.commit()
    return jsonify({'message': 'News added successfully!'})

if __name__ == '__main__':
    app.run()
