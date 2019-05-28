.PHONY: backend
.PHONY: frontend
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

runAllBackground :
	cd backend && \
	nodemon start &
	cd frontend && \
	npm run serve &

kill :
	killall -SIGKILL node
	killall -SIGKILL npm
	killall -SIGKILL sh