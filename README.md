# Python_Assignment4

This is Assignment 4 for advanced programming in python course, this program can build a web server with input text field, enter a coin name then after press check button it will return a bunch of paragraph related to entered coin from coinmarketcap.com also data will be saved in database

## Installation

Make sure that you have installed beautifulsoup4 , flask , sqlalchemy libraries and postgreSQL

```
pip install beautifulsoup4

pip install Flask

pip install Flask-SQLAlchemy

```

## Usage

Dowanload file and open Assignment4.py and make some changes
```
# connect to your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yourUsername:yourPassword@localhost/yourDBName'
```
## Example

After launch Assignment4.py you will have a link in terminal

```
http://127.0.0.1:5000/                              -- default page
http://127.0.0.1:5000/coin                          -- coin page
```
