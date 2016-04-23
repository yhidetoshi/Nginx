# Nginxでやった事
- installのFabric化
  - https://github.com/yhidetoshi/nginx/blob/master/nginx-install.py

- Wordpressを表示するための設定
   - https://github.com/yhidetoshi/nginx/blob/master/wordpress.conf

- Nginxの設定オプション
  - http://nginx.org/en/docs/http/ngx_http_upstream_module.html
 
- Reverse_Proxy / LB / SSL /Redirect等
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

