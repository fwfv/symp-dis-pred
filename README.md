## Disease Prediction System

This is a Stripped Down version of my final year project. It is in need of many improvements.

### Technologies Used

* Python
* Django
* Postgresql
* Machine Learning
* Html
* Css


### How to setup the project

This is how I set up the project in Debian Linux.

Linux or not it does not matter just adjust based on package names or applications.

#### Installing stuff

```
sudo apt update && sudo apt dist-upgrade
sudo apt install python3-venv python3-pip postgresql curl git
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
sudo apt install pgadmin4-web
sudo /usr/pgadmin4/bin/setup-web.sh
```

* Installing pgadmin is optional
* At the end you will be asked to give email and password
* You can give a non-real email address

> fakemail@email.com

* Just remember the email and password you will enter
* Answer "y" to the next few prompts

##### Setup Postgresql

```
sudo -iu postgres psql

CREATE DATABASE database_name;
CREATE USER username WITH PASSWORD 'password';
ALTER ROLE username SET client_encoding TO 'utf8';
ALTER ROLE username SET default_transaction_isolation TO 'read committed';
ALTER ROLE username SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
ALTER DATABASE database_name OWNER TO username;

\q
```

* first command is using default postgres user to log into the psql
* Fill the database_name with what you wish call your database
* Fill the username and password with your choice
* Replace all placeholders
* \q is to quit out of the psql

##### Add Postgresql To Pgadmin

* Log in to the Pgadmin web console at 127.0.0.1/pgadmin4
* Input email and password you set at the time of installation
* Click on Add new server
* Name :  Whatever you wish
* Click on Connection Tab
* Host name / Address :  localhost
* Maintainance database :  database_name (when setting up the postgresql in psql)
* Username :  username (when setting up postgresql in psql)
* Password :  password (when setting up postgresql in psql)
* Click Save

##### Setup virtualenv and Django

```
mkdir Project
cd Project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
django-admin startproject main .
python3 manage.py startapp app
```
