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

```
sudo apt update && sudo apt dist-upgrade
sudo apt install python3-venv python3-pip postgresql curl
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
