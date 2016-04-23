def nginx_install():
    with settings(warn_only="True"):
        result = run('ls /usr/sbin/nginx')
    if not result.succeeded:
        run('rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm')
        run('yum install -y nginx')
    if not exists("/etc/nginx/conf.d/sites-available"):
        run('mkdir -p /etc/nginx/conf.d/sites-available')
        put(local_path = REPO_PATH + 'apigee_module/nginx/available/*.conf',remote_path = '/etc/nginx/conf.d/sites-available')
    if not exists("/etc/nginx/conf.d/sites-enabled"):
        run('mkdir -p /etc/nginx/conf.d/sites-enabled')
        with cd('/etc/nginx/conf.d/sites-enabled'):
            run('ln -s ../sites-available/*.conf .')
    put(local_path = REPO_PATH + 'apigee_module/nginx/nginx.conf',remote_path = '/etc/nginx')

    run('chkconfig nginx on')
    run('chkconfig --list nginx')
    run('service nginx start')
