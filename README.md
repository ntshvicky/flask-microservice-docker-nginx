# This API is an example for Microservice Integration on Docker, with Python Flask, and webserver as Nginx and Gunicorn
Flask - Python micro framework for api development
Openapi - Swagger format for Flask
Nginx - Main Webserver to handle load balancing
Gunicorn - Python WSGI HTTP server for unix
Docker - Used for container


# What you need to do
1. This is an example code, so modify code as per your need
2. Define load balancing in nginx upstream
3. Write docker image (Dockerfile) for all APIs URL in different PORT
4. check my docker-compose code for docker config
    a. master api is main api, you can access on 80 port. In docker it is running on 3001 port
    b. master api will call another api
    c. employee api is running on 3002 port
    d. payroll based api is running on 3003 port
    You can make you project like, as per your requirements. Like for HRMS, employee management in port 3002, payroll in port 3003, inventory in port 3004, etc. Same in hospital management, different department different port. But one main/master api to intgerate with them.

Note: I will suggest, Database create outside docker. Or like some service provided by cloud services like Firebase, RDS, DynamoDB etc. FTP also, Like s3 bucket, your private FTP server.

