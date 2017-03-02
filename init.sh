sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s  /home/box/web/etc/gunicorn.conf /etc/init.d/gunicorn.conf
sudo /etc/init.d/gunicorn restart