#!/usr/bin/env python3
from fabric.api import *
import sys

env.hosts= ["ubuntu@34.239.250.176", "ubuntu@52.201.211.251"]
env.password = "password"


def install_nginx():
    sudo("apt-get update")
    sudo("apt-get install -y nginx")

def make_directories():
    sudo("mkdir -p /data/web_static/shared/")
    sudo("mkdir -p /data/web_static/releases/test/")
    sudo("echo 'Testing Static' | tee /data/web_static/releases/test/index.html")

def make_link():
    sudo("rm -rf /data/web_static/current")
    sudo("ln -s /data/web_static/releases/test /data/web_static/current")

def change_owner():
    sudo("chown -R ubuntu:ubuntu /data/")

def config_server():
    host_name = run("hostname")
    config = """
    server {
        listen 80;
        listen [::]:80;

        add_header X-Served-By "%s";

        server_name mojalefakodisang.tech www.mojalefakodisang.tech;

        location /hbnb_static/ {
            alias /data/web_static/current/;
        }
    }""" % host_name
    sudo(f"echo '{config}' > /etc/nginx/sites-available/default")

def restart_web_server():
    sudo("service nginx restart")

def deploy():
    install_nginx()
    make_directories()
    make_link()
    change_owner()
    config_server()
