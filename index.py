from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import jsonify
from flask import Blueprint,request

from DataStore.MySQLClient import MySQLClient
dns = {
    'user': 'root',
    'host': 'localhost',
    'password':'mysql',
    'database': 'mysql'
}
db = MySQLClient(**dns)

# Webページとしてのルーティングルール
app = Flask(__name__)

# RESTfulAPIのBlueprint作成,<http://host/api>以下のものはここのルールで処理される
api = Blueprint('api',__name__,url_prefix='/api')

# ------------------------------------------------------------------
@app.route("/")
def main():
    props = {'title': 'FlaskAPI - index', 'msg': 'Welcome to Index Page.'}
    html = render_template('index.html', props=props)
    return html

@app.route('/hello')
def hello():
    props = {'title': 'FlaskAPI - hello', 'msg': 'Hello World.'}
    html = render_template('hello.html', props=props)
    return html

@app.route('/users')
def users():
    props = {'title': 'Users List', 'msg': 'Users List'}
    stmt = 'SELECT * FROM USER_TBL'
    users = db.query(stmt)
    html = render_template('users.html', props=props, users=users)
    return html

@app.route('/users/<int:id>')
def user(id):
    props = {'title': 'User Information', 'msg': 'User Information'}
    stmt = 'SELECT * FROM USER_TBL WHERE ID = ' + str(id)
    user = db.query(stmt, id, prepared=False)
    html = render_template('user.html', props=props,user=user[0])
    return html

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('main'))

# ------------------------------------------------------------------
@app.route('/api/hello')
def helloget():
    return jsonify({'message':'Hello World.'})

@app.route('/apis/users')
def usersget():
    stmt = 'SELECT * FROM USER_TBL'
    users = db.query(stmt)
    json = {
        "users" : [{
            "ID" : user[0],
            "Name" : user[1]
        } for user in users]
    }
    return jsonify(json)


# エラーのハンドリング errorhandler(xxx)を指定、複数指定可能
# ここでは400,404をハンドリングする
@api.errorhandler(400)
@api.errorhandler(404)
def error_handler(error):
    # error.code: HTTPステータスコード
    # error.description: abortで設定したdict型
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code
# ------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)