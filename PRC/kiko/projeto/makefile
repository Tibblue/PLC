.PHONY: backend frontend
.PHONY: graphdb json_server
.PHONY: runAllBackground
.PHONY: kill

### Runners
# exec GraphDB (using docker)
graphdb :
	docker run -p 7200:7200 tibblue/graphdb_prc:v3.0

# exec json-server (User Database)
json_server :
	cd usersdb && \
	npm run json:server

# exec backend (Node)
backend :
	cd backend && \
	nodemon start

# exec frontend (Vue)
frontend :
	cd frontend && \
	npm run serve

# exec userDB & backend & frontend (in background)
runAllBackground :
	cd usersdb && \
	npm run json:server &
	cd backend && \
	nodemon start &
	cd frontend && \
	npm run serve &

### Killers
kill :
	killall -SIGKILL node
	killall -SIGKILL npm
	# killall -SIGKILL sh
