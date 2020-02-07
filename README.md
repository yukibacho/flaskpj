# FlaskRestPJ

PythonのWebフレームワークであるFlask(フラスコ)の勉強用リポジトリ。<br>
DockerのMySQLコンテナのDBのレコードを操作します。<br>
※現状ではjsonを返さず、Webページ上で結果を表示しています。<br>
Docker,Pythonともに初心者なのでプルリク等気軽にお願い致します。

# Dockerの環境構築方法<br>
(1)Docker Desktop for Windowsをinstall<br>
⇒install前にHyperVをコントロール パネル\すべてのコントロール パネル項目\プログラムと機能で有効化。<br>
⇒install時にout of memoryでと出てきたらDockerのSettingを開き、Resourcesタブのメモリーを減らす。

(2)本プロジェクトのフォークしてローカルにクローン<br>

(3)docker-composeを使用してコンテナを作成<br>
>クローンしたディレクトリに移動し、<br>
$docker-compose up -d

~docker-composeを使用しない例~<br>
(2)ローカルのPowerShellにてMySQLコンテナのイメージをプル<br>
>$docker pull mysql<br>

(3)プルしたイメージからコンテナ作成<br>
>$docker run --name mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql:latest<br>
※rootユーザのパスワードをmysql設定。使用ポートは3306。コンテナ名はmysql。<br>

# DB運用方法（コンテナ内部でDBの設定をしたい場合など）<br>
(1)コンテナIDを調べる<br>
>$docekr ps <-a>  <br>

|CONTAINER ID|IMAGE|COMMAND|CREATED|STATUS|PORTS|NAMES|
|---|---|---|---|---|---|---|
|8b8be3a1e9fa|mysql:latest|"docker-entrypoint.s…"|2 days ago|Up 4 seconds|0.0.0.0:3306->3306/tcp, 33060/tcp|mysql|

※aオプションを付けると起動していないコンテナも表示される

(2)コンテナに接続<br>
>$docker exec -it mysql bash<br>

(3)コンテナ内でDBに接続(コンテナに接続した状態で)<br>
>$mysql -u root -p<br>
Enter password:mysql<br>

(4)Dockerコンテナを落とす、起動する<br>
>落とす<br>
>$docker stop mysql<br>
起動する<br>
>$docker start mysql<br>
再起動する<br>
>$docker restart mysql<br>



# Flask開発環境構築方法<br>
(1) Pythonダウンロード、インストール
>https://www.python.org/downloads/release/python-381/<br>
⇒Windows x86-64 web-based installer

(2)Flaskをインストール
>$pip install flask
