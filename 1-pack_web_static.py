#!/usr/bin/env python3
"""
script to pack an archive using fabric
"""

import datetime
from fabric.api import *

def do_pack():
    """
    function to pack a .tgz archive
    """

    time = datetime.now()

    str_time = time.strftime(%Y%m%d%h%m%s)
    local( 'sudo mkdir -p /versions')

    local("tar -cvzf versions/web_static_{}.tgz web_static".format(str_time))

