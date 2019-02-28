from fabric.api import *

env.hosts='127.0.0.1'
env.user='vagrant'
env.password='vagrant'

def ciserver():
     sudo("apt update -y")
     sudo("apt-get install openjdk-8-jdk -y")
     sudo("apt-get  install git -y")
     with cd("/root"):
          sudo("git clone -b vp-memcached-rabbitmq https://github.com/wkhanvisualpathit/VProfile.git")
          sudo("apt-get install maven -y")
     with cd("/root/VProfile"):
          sudo("sed -i 's/password=password/password=root/g' src/main/resources/application.properties")
          sudo("sed -i 's/newuser/root/g' src/main/resources/application.properties")
          sudo("sed -i 's/localhost:3306/db.com:3306/' src/main/resources/application.properties")
          sudo("sed -i 's/address=127.0.0.1/address='rmq.com'/' src/main/resources/application.properties")
          sudo("sed -i 's/active.host=127.0.0.1/active.host='memcache.com'/' src/main/resources/application.properties")
          sudo("mvn clean install")


def appserver():
     sudo("apt-get update -y")
     sudo("apt-get install openjdk-8-jdk -y")
     sudo("apt-get install wget -y")
     with cd("/root"):
         sudo("wget http://redrockdigimark.com/apachemirror/tomcat/tomcat-8/v8.5.31/bin/apache-tomcat-8.5.31.tar.gz")
         sudo("mv apache-tomcat-8.5.31.tar.gz /opt/apache-tomcat-8.5.31.tar.gz")
     with cd("/opt"):
          sudo("tar -xvzf apache-tomcat-8.5.31.tar.gz")
          sudo("rm -rf /opt/apache-tomcat-8.5.31/webapps/ROOT")
          sudo("cp /root/VProfile/target/vprofile-v1.war /opt/apache-tomcat-8.5.31/webapps/ROOT.war")
          sudo("systemctl stop ufw")
          sudo("ufw disable")
          sudo("/opt/apache-tomcat-8.5.31/bin/startup.sh")
    


def db_server():
     sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'")
     sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'")
     sudo("apt-get update")
     sudo("apt-get install mysql-server -y")
     sudo("sed -i 's/127.0.0.1/0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf")
     sudo("mysql -u root -e \"create database accounts\" --password='root';")
     sudo("mysql -u root -e  \"grant all privileges on *.* TO 'root'@'app.com' identified by 'root'\"  --password='root';")
     sudo("mysql -u root --password='root' accounts < /root/VProfile/src/main/resources/db_backup.sql;")
     sudo("mysql -u root -e \"FLUSH PRIVILEGES\" --password='root';")
     sudo("systemctl restart mysql")


def lb():
     sudo("apt-get install nginx -y")
     sudo("cp /root/vproapp /etc/nginx/sites-available/vproapp")
     sudo("rm -rf /etc/nginx/sites-enabled/default")
     sudo("ln -s /etc/nginx/sites-available/vproapp /etc/nginx/sites-enabled/vproapp")
     sudo("sudo systemctl restart nginx")


def rabbitmq():
     sudo("echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list")
     sudo("wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -")
     sudo("wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc| sudo apt-key add -")
     sudo("apt-get install rabbitmq-server -y")
     sudo("echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config")
     sudo("rabbitmqctl add_user test test")
     sudo("rabbitmqctl set_user_tags test administrator")

def memcache():
     sudo("apt-get install memcached -y")
     sudo("systemctl start memcached")
     sudo("memcached -p 11111 -U 11111 -u memcache -d")        

