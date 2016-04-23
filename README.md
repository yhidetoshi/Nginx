![Alt Text](https://github.com/yhidetoshi/Pictures/raw/master/Nginx/nginx-icon.png)

### Nginxでやった事


**[インストール(構築)]**

|方法    |リンク         |
|:-----------|:------------|
|手動|インストール手動|
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
```
upstream backend-prod 
{ 
    //LB Reverse_proxy
  	server ip_address:port_num max_fails=3 fail_timeout=10s; 
	  server ip_address:port_num max_fails=3 fail_timeout=10s; } 
	
	server 
	{
	    //SSL
	    listen 443; 
	    server_name ssl on;
	    ssl_certificate /etc/nginx/conf.d/server.crt; 
	    ssl_certificate_key /etc/nginx/conf.d/server.key;
	}
    
    location / {
       proxy_pass http://backend-jenkins;
      break;
    }
    	// hogehuga 何らかの処理とか
}
```

