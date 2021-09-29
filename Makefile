COMPOSE = fades -d docker-compose==1.24 -x docker-compose -f docker-compose.yml

help:
	@echo "help             -- print this help"
	@echo "build            -- build docker environment"
	@echo "stop             -- stop docker stack"
	@echo "up               -- starts docker stack"
	@echo "ps               -- show status"

stop:
	$(COMPOSE) stop

up:
	$(COMPOSE) up

upd:
	$(COMPOSE) up -d

logs:
	$(COMPOSE) logs --follow

pull:
	$(COMPOSE) pull

ps:
	$(COMPOSE) ps

build:
	./build_docker_images.sh

remove-pycache:
ifneq ($(EUID),0)
	find . -name "__pycache__" | xargs sudo rm -rf
else
	find . -name "__pycache__" | xargs rm -rf
endif

remove-dbs:
	rm -rf ground/db.sqlite3 satellites_app/db.sqlite3

clean: stop remove-pycache remove-dbs
	$(COMPOSE) rm --force -v

down:
	${COMPOSE} down -v --remove-orphans

migrate_ground:
	$(COMPOSE) run --rm ground python /code/manage.py migrate

migrate_8081:
	$(COMPOSE) run --rm satellite_8081 python /code/manage.py migrate

migrate_8082:
	$(COMPOSE) run --rm satellite_8082 python /code/manage.py migrate

bootstrap: migrate_ground migrate_8081 migrate_8082

ground-shell:
	$(COMPOSE) run --rm ground /bin/bash

satellite-8081-shell:
	$(COMPOSE) run --rm satellite_8081 /bin/bash

satellite-8082-shell:
	$(COMPOSE) run --rm satellite_8082 /bin/bash

setup_8081:
	$(COMPOSE) run --rm tools python /code/setup_satellite.py --host satellite.8081 --port 8081

setup_8082:
	$(COMPOSE) run --rm tools python /code/setup_satellite.py --host satellite.8082 --port 8082

setup_satellites: setup_8081 setup_8082

tools-shell:
	$(COMPOSE) run --rm tools /bin/bash

.PHONY: help build stop up updb upd pull ps remove-pycache clean
