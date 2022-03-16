# Varapp BIBBOX application

This container can be installed as [BIBBOX APP](http://bibbox.readthedocs.io/en/latest/admin-documentation/ "BIBBOX App Store") or standalone. 

* after the docker installation follow these [instructions](https://github.com/bibbox/app-redcap/blob/master/INSTALL-APP.md)

## Standalone Installation

Clone the github repsoitory and start the install.sh. If necessary change the ports and volume mounts in `docker-compose.yml`.  

`sudo git clone https://github.com/bibbox/app-varapp

`sudo chmod +x install.sh`

`sudo ./install.sh`

default login admin/admin

## Install within BIBBOX

The BIBBOX framework can be installed 
* as a [virtual machine](http://bibbox.bbmri-eric.eu/resources/machine/), 
* using [vagrant/puppet](http://bibbox.readthedocs.io/en/latest/installation-vagrant/) 
* are on any Ubuntu System following these [instructions](http://bibbox.readthedocs.io/en/latest/installation-source/)  

After BIBBOX is up and running, you can use the [BIBBOX APP Store](http://bibbox.readthedocs.io/en/latest/admin-documentation/ "BIBBOX App Store") to install a lot of software tools. 

default login admin/admin

## Docker Images Used


 * [bibbox/varapp-frontend](https://hub.docker.com/r/bibbox/varapp-frontend)
 * [sibswiss/varapp-backend](https://hub.docker.com/r/sibswiss/varapp-backend), offical container
 * [mariadb](https://hub.docker.com/_/mariadb), offical mariadb container
 * [redis](https://hub.docker.com/_/redis), offical redis container
 
## Database information

- DB_PASSWORD: pwd
- SECRET_KEY: K6QKN6C2xtcl.

## Mounted Volumes

- ./data/mysql-data-volume
- ./data/resources/db
- ./data/varmed/settings


