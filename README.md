# Flou Server API

- FastAPI + Asyncio
- SQLModel for data models and validation
- Celery for background tasks
- Alembic for migrations
- Supertokens for user authentication
- Mypy for type checking
- Make for running commands

Additionally, the codebase showcases the following things:

- Multiple FastAPI apps in one project
- Alembic auto-generating migrations from model files
- Celery tasks communicating through an SQS FIFO queue
- AWS S3 integration for storing images
- Loggers that print SQL queries and other useful information
- Error handler middlewares
- CORS middleware
- Two separate types of authentication (static auth token for an internal endpoint + Supertokens for user authentication)
- Dependencies management using Poetry
- And more.

## Project structure

The project is organized into the following directories and files:

| Directory/File Name | Description                                                                          |
| ------------------- | ------------------------------------------------------------------------------------ |
| background_tasks/   | Celery tasks                                                                         |
| crud/               | CRUD operations                                                                      |
| db/                 | Alembic migrations                                                                   |
| models/             | model files that combine data models and Pydantic schemas                            |
| schemas/            | Pydantic schemas for things other than data models (e.g. api requests and responses) |
| services/           | business logic                                                                       |
| subapps/            | FastAPI apps with each file containing a separate app                                |
| utils/              | utility functions                                                                    |
| celery.py           | Celery app                                                                           |
| config.py           | Pydantic settings                                                                    |
| database.py         | SQLAlchemy database engine and session                                               |
| dependencies.py     | FastAPI dependencies                                                                 |
| main.py             | main project file                                                                    |

## Running the project

### Steps

1. Clone the repo
2. Change `sqlalchemy.url` in `alembic.ini` to point to your database
3. Use commands in Makefile to install dependencies and run migrations
4. Rename `.env.example` to `.env` and fill in the values
5. Run `make server` and `make worker` to start the web server and the Celery worker

## Pre-Commit Setup

If you are using this project then pre-commit setup would be very helpful for checking your codebase. In short, pre-commit is a tool that allows developers to define and apply automated checks to their code before they commit it to a version control system. You can find more info [here](https://pre-commit.com)

```commandline
pre-commit install

# for the first time, run on all files
pre-commit run --all-files
```

## License

MIT License
