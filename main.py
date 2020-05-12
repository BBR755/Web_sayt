from flask import Flask,  render_template
#from data import db_session
#from data.users import User
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


#def main():
#    print(1111)
#    app.run()
#   print(2222)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
