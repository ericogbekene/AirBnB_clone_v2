#!/usr/bin/env bash
#setup server with configurations

sudo apt-get -y update
sudo apt install -y nginx

#create necessary directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/releases/test/index.html
echo "Hello there old friend" > /data/web_static/releases/test/index.html

#create symbolic link
ln -T /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/
sudo service nginx restart

#cp /etc/nginx/sites-enabled/default www/data/web_static/current/
