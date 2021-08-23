# Product Label Data Extraction Tool

## Setup local development environment (with docker)

1. Add .env file:
   `cp .env.dev.sample .env`
2. Run project <br>
   `docker-compose up` <br>
    Access url: http://127.0.0.1:8000/

## Administrative commands
`docker-compose run --rm backend <<COMMAND>>`
### Exemples

#### create superuser
`docker-compose run --rm backend  python manage.py createsuperuser`
#### Run black
`docker-compose run --rm backend black .`
#### Run flake8
`docker-compose run --rm backend flake8 .`