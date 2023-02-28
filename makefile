export MONGODB_URL="mongodb://root:example@localhost/local?retryWrites=true&w=majority&authSource=admin"

SHELL := /bin/bash

mongo_db_url: 
	@echo $$MONGODB_URL

mongo_setup:
	docker-compose up