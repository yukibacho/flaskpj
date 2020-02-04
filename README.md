# flaskpj
PythonのWebフレームワークであるFlask(フラスコ)の勉強用リポジトリ。<br>
MySQLコンテナのDBのレコードを操作します。<br>
※現状ではjsonを返さず、Webページ上で結果を表示しています。<br>
Python初心者なのでプルリク等気軽にお願い致します。

# イメージ図
![FlaskImage](https://user-images.githubusercontent.com/57794992/73734710-663f5000-4781-11ea-9ece-8861c6188bf0.png)

# DBについて
DockerでMySQLコンテナを作成して本アプリ上からアクセスしています。
>$docker pull mysql<br>
$docker run --name mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql:latest

後はコンテナ内にdocker execコマンドで接続し、DBにテーブルを作っています。<br>
テーブル作成に用いたSQLクエリ(user_tbl_create.sql )はリポジトリにアップされています。
