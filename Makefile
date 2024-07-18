install:
		pdm install

server:
		uvicorn flou_server.main:app --reload

worker:
		celery -A flou_server.celery worker --loglevel=info --concurrency=5

lint:
		mypy flou_server

migration_generate:
		alembic revision -m "$(name)"

migration_autogenerate:
		alembic revision --autogenerate -m "$(name)"

migrate:
		alembic upgrade head

rollback:
		alembic downgrade -1

rollback_base:
		alembic downgrade base

reset:
		make rollback migrate seed
