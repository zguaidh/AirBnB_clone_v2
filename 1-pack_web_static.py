#!/usr/bin/python3
"""
Module that archives files
"""
import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """Packs the static files"""
    env.hosts = "localhost"
    now = datetime.now()
    f_now = now.strftime("%Y%m%d%H%M%S")
    path = f"versions/web_static_{f_now}.tgz"
    local("mkdir -p versions")
    result = local(f"tar -cvzf {path} web_static", capture=True)
    if not result.return_code:
        return f"versions/{path}"
    return None
