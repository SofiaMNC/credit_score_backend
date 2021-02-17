# Credit Scoring Web App - Backend
*Sofia Chevrolat (December 2020)*

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://madimedia.pro)

![](https://img.shields.io/badge/USES-Docker-2496ED?style=for-the-badge&logo=Docker)

![](https://img.shields.io/badge/REST_API_SERVER-Heroku-430098?style=for-the-badge&logo=Heroku)
![](https://img.shields.io/badge/DOCUMENTED_WITH-Swagger-85EA2D?style=for-the-badge&logo=Swagger)

## Overview
This is the backend of the credit scoring web app. 
It provides a REST API by which to access relevant data for each anonymized client.
It uses a machine learning model created using the Home Credit Default Risk dataset provided by the Home Credit Group.

The backend uses WSGI and Flask, and accesses static data stored on an Amazon S3 bucket.
The server stubs were generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project, using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki).  

## Requirements
connexion[swagger-ui] 2.7.0

python_dateutil 2.6.0+

setuptools 21.0.0

Werkzeug 1.0.0

joblib 0.14.1

lightgbm 3.0.0

pandas 1.0.1

requests 2.22.0

## Usage
### Without Docker
To run the server, please execute the following from the root directory:

```bash
pip3 install -r requirements.txt
python3 -m swagger_server
```

When the server is run locally:
- it is accessible here:

    ```
    http://localhost:8080/v2/
    ```

- the documentation for the API is accessible here: 

    ```
    http://localhost:8080/v2/ui/
    ```

### With Docker
To run the web app using a Docker container, please execute the following from the root directory:

```bash
docker build -t api_server .
docker run -d --name api_server -p 8080:8080 api_server
```
