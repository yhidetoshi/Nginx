![Alt Text](https://github.com/yhidetoshi/Pictures/raw/master/Nginx/nginx-icon.png)

### Nginxでやった事


**[インストール(構築)]**

|方法    |リンク         |
|:-----------|:------------|
|手動|https://github.com/yhidetoshi/Nginx/blob/master/README.md#nginxのインストール手動|
|Chef|https://github.com/yhidetoshi/chef_mac/tree/master/cookbooks/nginx|
|Fabric|https://github.com/yhidetoshi/Nginx/blob/master/install-by-fabric/nginx-install.py|
|Docker|https://github.com/yhidetoshi/Docker#mac環境でnginxjenkinsをリバースプロキシ環境を構築する|

**[Reverse_Proxy / LB / SSL /Redirect等の設定例]**

-> https://github.com/yhidetoshi/Nginx/tree/master/conf

#### Nginxのインストール(手動)
- packageでインストールする
```
# rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
# yum -y install nginx
# service nginx start
```
- ソースコードからインストールする
```
- ビルドに必要なライブラリ:PCRE/zlib/OpenSSL
- http://nginx.org/en/download.htmlからMainline versionをダウンロードする
- ソースをダウンロードしたら, ./configure, make, make installを順に実行
- PATHを通す：$ export PATH=/usr/local/nginx/sbin:$PATH
```

|コマンド(#service)|役割         |
|:----------------|:------------|
|nginx start|nginxを再起動する|
|nginx stop|nginxを停止する|
|nginx restart|nginxを再起動する|
|nginx reload|nginxの設定を再読み込みする|
|nginx configtest|nginxの設定ファイルの構文をチェック|
|nginx upgrade|nginxの実行バイナリを無停止で差し替える|
