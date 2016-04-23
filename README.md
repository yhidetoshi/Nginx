![Alt Text](https://github.com/yhidetoshi/Pictures/raw/master/Nginx/nginx-icon.png)

### Nginxでやった事


**[インストール(構築)]**

|方法    |リンク         |
|:-----------|:------------|
|手動|https://github.com/yhidetoshi/Nginx/blob/master/README.md#nginxのインストール手動|
|Chef|https://github.com/yhidetoshi/chef_mac/tree/master/cookbooks/nginx|
|Fabric|https://github.com/yhidetoshi/Nginx/blob/master/install-by-fabric/nginx-install.py|
|Docker|https://github.com/yhidetoshi/Docker#mac環境でnginxjenkinsをリバースプロキシ環境を構築する|

#### Nginxのインストール(手動)
```
# rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
# yum -y install nginx
# service nginx start
```

**[Reverse_Proxy / LB / SSL /Redirect等の設定例]**

-> https://github.com/yhidetoshi/Nginx/tree/master/conf

