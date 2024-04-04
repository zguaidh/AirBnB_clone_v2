#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# Install NGINX web server
if ! command -v nginx &> /dev/null
then
	apt-get update
	apt-get install nginx
fi

# Create /data/ directory
mkdir -p /data/web_static/shared /data/web_static/releases/test/

# Create a test HTML file
printf '%s\n' "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html
" > /data/web_static/releases/test/index.html

# Creates a link between files
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership of /data/ directory
chown -hR ubuntu:ubuntu /data/

# Configure config file
host_name=$(hostname)
printf '%s\n' "
server {
	listen 80;
	listen [::]:80;

	add_header X-Served-By \"$host_name\";

	server_name mojalefakodisang.tech www.mojalefakodisang.tech;
	root /var/www/html;
	index index.html index.htm;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html index.htm 0-index.html;
	}

	error_page 404 /404.html;

	location /404 {
		root /var/www/html;
		internal;
	}
}" > /etc/nginx/sites-available/default

# Start NGINX server
service nginx start
