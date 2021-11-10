from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:er2003618@localhost/PythonFlask'

db = SQLAlchemy(app)

class Coin(db.Model):
    __tablename__ = 'coin'

    id = db.Column('id', db.Integer, primary_key=True)
    coin_name = db.Column('coin_name', db.Unicode)
    text = db.Column('paragraph', db.TEXT)

    def __init__(self, id, coin_name, text):
        self.id = id
        self.coin_name = coin_name
        self.text = text

@app.route('/coin', methods=['POST', 'GET'])
def coin():

    tagArray = []
    if request.method == 'POST':
        inputCoin = request.form['coin']
        url = 'https://coinmarketcap.com/currencies/' + inputCoin + '/'
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        for tags in soup.find_all('p'):
             tagArray.append(tags.text)

        obj = Coin.query.all()
        lastId = obj[-1].id

        new_coin = Coin(lastId+1, inputCoin, tagArray)
        db.session.add(new_coin)
        db.session.commit()

        coinInfo = Coin.query.filter_by(id=lastId+1).first()
        txt = coinInfo.text
        list = txt.split('","')

        return render_template('index.html', content=list)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

