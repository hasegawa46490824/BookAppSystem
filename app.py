from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

#どのDBを使うかそのDBの名前を決定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#変更追跡機能の無効化
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#flaskにsqlAlchemyを接続
db = SQLAlchemy(app)

#テーブルの作成 classを作ったら自動で作成できる。
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

#データベースの作成
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    books = Book.query.all()
    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(debug=True , host="127.0.0.1" , port = 5000)
