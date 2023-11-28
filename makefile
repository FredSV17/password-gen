SHELL := /bin/bash

mongo_db_url: 
	export MONGODB_URL := mongodb://root:example@localhost/local?retryWrites=true&w=majority&authSource=admin
	@echo $$MONGODB_URL

mongo_setup:
	docker-compose up
	
	
	  api:
    build: ./passgen_webscaper
    ports: 
      - "80:80"
    environment:
      MONGODB_URL: "mongodb://root:example@mongo:27017/local?retryWrites=true&w=majority&authSource=admin"
      API_TEST: 0
    networks:
      - db-network
