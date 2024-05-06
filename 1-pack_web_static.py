#!/usr/bin/python3
"""
Module that genereate tgz archive
Usage: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """

    now = datetime.now()
    archive = 'web_static_' + now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(archive))
    if result is not None:
        return archive
    else:
        return None
