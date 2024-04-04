#!/usr/bin/python3
"""
Module that archives files
"""
import os
from fabric.api import *
from datetime import datetime
env.hosts = ["34.239.250.176", "52.201.211.251"]


def do_deploy(archive_path):
    """Deploys the web static"""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, name)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(name)).failed is True:
        return False
    symlink = "/data/web_static/current"
    run(f"rm -rf {symlink}")
    if run("ln -s /data/web_static/releases/{}/ {}".
            format(name, symlink)).failed is True:
        return False
    return True
