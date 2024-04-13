## Sellcord Assessment Task

Django based application to track disputes and returns raised by customers.


Install Docker and Docker compose for your respective environment
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

copy environment files and update the environment values, then run docker compose up 

                        cp .env.dev.example .env.dev
                        docker compose up


for creating customers, orders and disputes - check [Assessment Task.postman_collection.json](https://github.com/ousat/sellcord-assessment-task/blob/master/Assessment%20Task.postman_collection.json)

APIs only allow you to create disputes and returns, to edit - a staff/admin user should log into `/admin` console and update the values 


the following path would let you view disputes loading via htmx - `/disputes`


### Architectural Overview - 
            This is a simple django project using postgreSQL DB and docker. Consists of four tables.


