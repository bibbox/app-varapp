# Varapp BIBBOX application

This container can be installed as [BIBBOX APP](https://bibbox.readthedocs.io/en/latest/) or standalone. 

* After the docker installation follow these [instructions](INSTALL-APP.md)

## Standalone Installation

Clone the github repsoitory and start the install.sh. If necessary change the ports and volume mounts in `docker-compose.yml`.  

`sudo git clone https://github.com/bibbox/app-varapp`

`sudo chmod +x install.sh`

`sudo ./install.sh`

Default **login** `admin`/`admin`

You can access varapp via your webbrowser at [http://localhost:8080](http://localhost:8080).
Finish your varapp setup by following these [instructions](INSTALL-APP.md).

## Install within BIBBOX

Within BIBBOX you can use the [BIBBOX](https://bibbox.readthedocs.io/en/latest/) to install a lot of software tools. After the installation is finished you can start your application in the dashboard.

Default **login** `admin`/`admin`

Finish your varapp setup by following these [instructions](INSTALL-APP.md).


## Docker Images Used


 * [bibbox/varapp-frontend](https://hub.docker.com/r/bibbox/varapp-frontend)
 * [sibswiss/varapp-backend](https://hub.docker.com/r/sibswiss/varapp-backend), offical container
 * [mariadb](https://hub.docker.com/_/mariadb), offical mariadb container
 * [redis](https://hub.docker.com/_/redis), offical redis container
 
## Database information

- DB_PASSWORD: `pwd`
- SECRET_KEY: `K6QKN6C2xtcl.`

## Mounted Volumes

- ./data/mysql-data-volume
- ./data/resources/db
- ./data/varmed/settings


