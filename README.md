# FlaskRestPJ

PythonのWebフレームワークであるFlask(フラスコ)の勉強用リポジトリ。<br>
DockerのMySQLコンテナのDBのレコードを操作します。<br>
※現状ではjsonを返さず、Webページ上で結果を表示しています。<br>
Docker,Pythonともに初心者なのでプルリク等気軽にお願い致します。

# イメージ:<br>
![FlaskImage](/uploads/d88733aa1dab937b75b17ddca4cd0aef/FlaskImage.png)


# Dockerの環境構築方法<br>
(1)Docker Desktop for Windowsをinstall<br>
⇒install前にHyperVをコントロール パネル\すべてのコントロール パネル項目\プログラムと機能で有効化。<br>
⇒install時にout of memoryでと出てきたらDockerのSettingを開き、Resourcesタブのメモリーを減らす。

(2)DockerのSetting/Docker EngineタブでDaemonコンフィグファイルを編集<br>
>{<br>
  "registry-mirrors": [<br>
    "https://nexus.intra.oki.co.jp:5000"<br>
  ],<br>
  "insecure-registries": [<br>
    "harbor.intra.oki.co.jp",<br>
    "nexus.intra.oki.co.jp:5000"<br>
  ],<br>
  "debug": true,<br>
  "experimental": false<br>
}

参考:<br>
https://gitlab.intra.oki.co.jp/docker/windows10<br>

(3)本プロジェクトのフォークしてローカルにクローン<br>

(4)docker-composeを使用してコンテナを作成<br>
>クローンしたディレクトリに移動し、<br>
$docker-compose up -d

~docker-composeを使用しない例~<br>
(3)ローカルのPowerShellにてMySQLコンテナのイメージをプル<br>
>$docker pull mysql<br>

(4)プルしたイメージからコンテナ作成<br>
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

(2)コマンドラインでプロキシ設定
>$pip config set global.trusted-host nexus.intra.oki.co.jp<br>
>$pip config set global.index-url http://nexus.intra.oki.co.jp/repository/pypi/simple/

(3)Flaskをインストール
>$pip install flask
