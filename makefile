SHELL := /bin/bash

mongo_db_url: 
	export MONGODB_URL := mongodb://root:example@localhost/local?retryWrites=true&w=majority&authSource=admin
	@echo $$MONGODB_URL

mongo_setup:
	docker-compose up
