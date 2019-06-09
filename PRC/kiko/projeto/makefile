.PHONY: backend
.PHONY: frontend
.PHONY: graphdb
.PHONY: runAllBackground
.PHONY: kill

# exec backend (Node)
backend :
	cd backend && \
	nodemon start

# exec frontend (Vue)
frontend :
	cd frontend && \
	npm run serve

graphdb :
	docker run -p 7200:7200 tibblue/graphdb_prc:v3.0

runAllBackground :
	cd backend && \
	nodemon start &
	cd frontend && \
	npm run serve &

kill :
	killall -SIGKILL node
	killall -SIGKILL npm
	killall -SIGKILL sh
