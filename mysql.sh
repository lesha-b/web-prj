sudo /etc/init.d/mysql start

mysql -uroot -e "create database jj;"
mysql -uroot -e "create user 'jj@localhost' identifiedby 'pas579';"
mysql -uroot -e "grant all on jj.* to 'jj@localhost';"
mysql -uroot -e "flush privilegs;"