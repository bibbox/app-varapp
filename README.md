# varapp BIBBOX application

This container can be installed as [BIBBOX APP](https://bibbox.readthedocs.io/en/latest/ "BIBBOX App Store") or standalone. 

- after the docker installation follow these [instructions](INSTALL-APP.md)

## Standalone Installation 

Clone the github repository. If necessary change the ports in the environment file `.env` and the volume mounts in `docker-compose.yml`.


```
git clone https://github.com/bibbox/app-varapp
cd app-varapp
docker-compose up -d
```

The main App can be opened and set up at

```
http://localhost:8000
```


Default **login** `admin`/`admin`


## Install within BIBBOX

Visit the BIBBOX page and find the App by its name in the Store. Click on the symbol and select Install. Then fill the parameters below and name your app click install again.

## Docker Images used
  - [sibswiss/varapp-backend](https://hub.docker.com/r/sibswiss/varapp-backend) 
  - [bibbox/varapp-frontend](https://hub.docker.com/r/bibbox/varapp-frontend) 
  - [mariadb](https://hub.docker.com/r/mariadb) 
  - [redis](https://hub.docker.com/r/redis) 


 
## Install Environment Variables
  - DB_PASSWORD = Database Password
  - SECRET_KEY = SECRET KEY

  
The default values for the standalone installation are:
  - DB_PASSWORD = pwd
  - SECRET_KEY = changethissecretkeyinproductionenvironments

  
## Mounted Volumes
### sibswiss/varapp-backend Conatiner
  - *${GEMINI_DB_PATH:-./data/resources/db}:/db*
  - *${SETTINGS_PATH:-./data/varmed/settings}:/app/varmed/settings*
  - *./data/init:/var/lib/mysql*
### mariadb Conatiner
  - *./data/mysql-data-volume:/var/lib/mysql*
