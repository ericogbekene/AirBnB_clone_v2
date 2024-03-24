#!/usr/bin/env python3
#script to deplot to server

from fabric.api import *

def do_deploy(archive_path):
    """
    deploy a script using fabric
    """


    if not archive_path:
        return False

    #env.user = 'ubuntu'
    #env.hosts = ['ubuntu@192.168.1.1', 'serverX']

    put ('versions/web_static_20240307130253.tgz', '/tmp/web_static_20240307130253.tgz')

    run ('sudo mkdir -p /data/web_static/releases/web_static_20240307130253/')

    run ('sudo tar -xzf /tmp/web_static_20240307130253.tgz -C /data/web_static/releases/web_static_20240307130253/')

    run ('sudo rm /tmp/web_static_20240307130253.tgz')

    run ('sudo ln -s /data/web_static/releases/web_static_20240307130253 /data/web_static/current')

    return True




