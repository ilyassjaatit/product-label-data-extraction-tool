# Product Label Data Extraction Tool

## Setup local development environment (with docker)

1. Add .env file:
   `cp .env.dev.sample .env`
2. Run project <br>
   `docker-compose up` <br>
    Access url: http://127.0.0.1:8000/ <br> flow url http://localhost:5555/
3. Run interactive mode pdb <br>
   `docker-compose up -d &   docker-compose stop backend & docker-compose run --rm --service-ports backend`
## Administrative commands
`docker-compose run --rm backend <<COMMAND>>`
### Exemples

#### create superuser
`docker-compose run --rm backend  python manage.py createsuperuser`
#### shell plus django
`docker-compose run --rm backend  python manage.py shell_plus`
#### Run black
`docker-compose run --rm backend black .`
#### Run flake8
`docker-compose run --rm backend flake8 .`

## Run tests
`docker-compose run --rm backend pytest`
