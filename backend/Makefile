include ../.env

run:
	uvicorn ${BACKEND_PORT} src.main:app
dev_server:
	uvicorn --host localhost --port ${BACKEND_PORT} src.main:app --reload