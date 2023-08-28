# Introduction
This is a simple API built using the Representational State Transfer (REST) architecture.

At the moment, this API only handles the GET method.

# Requirement
It is recommended to deploy as a docker container.

An alternative is to run the web application directly using Python virtual environment.

# Execution

### Docker

#### To Run

build the container
```
docker build -t rest-server .
```

run the container
```
docker run -dp 5000:5000 rest-server
```
The REST API should be accessible at http://127.0.0.1:5000/publications

#### To Stop

get the container id
```
docker ps
```

stop the container
```
docker stop [container id]
```
