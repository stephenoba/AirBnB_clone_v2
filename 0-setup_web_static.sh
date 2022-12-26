#!/usr/bin/env bash
# Script configures server and uploads static files

if ! [ -d "/data/web_static/shared/" ]
then
  mkdir -p /data/web_static/shared/
fi

if ! [ -d "/data/web_static/releases/test/" ]
then
  mkdir -p /data/web_static/releases/test/
fi

# test file to test configuration
echo "Hello, Universe!!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership to user and group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
