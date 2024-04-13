Sellcord Assessment Task


Install Docker and Docker compose for your respective environment
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

copy environment files and update the environment values, then run docker compose up 
            cp .env.dev.example .env.dev
            docker compose up


for creating customers, orders and disputes - check Assessment Task.postman_collection.json
can only create disputes and returns using APIs, to edit - a staff/admin user should log into /admin and update the values 


the following path would let you view disputes loading via htmx -
                    /disputes



