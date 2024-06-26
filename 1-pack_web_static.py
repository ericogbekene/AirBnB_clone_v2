#!/usr/bin/python3
"""
script to pack an archive using fabric
"""

import datetime
from fabric.api import *
import os


def do_pack():
    """
    function to pack a .tgz archive
    """

    time = datetime.datetime.now()

    str_time = time.strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p versions')

    local("sudo tar -cvzf versions/web_static_{}.tgz web_static"
          .format(str_time))

    path_file = "versions/web_static_{}.tgz"\
        .format(str_time)
    size_of_file = os.path.getsize(path_to_file)

    print("web_static packed: {} -> {}Bytes".format(path_file, size_of_file))

    return path_to_file
