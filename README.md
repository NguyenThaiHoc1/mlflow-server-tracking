# mlflow-server-tracking
This is a source code used to run server tracking

Run cmd
> docker-compose up web -d --build

Sever tracking is public at port 5000
> localhost:5000 

S3-Minio-Bucket at port 9002
> localhost:9002

# Infomation about scenario

This project built follow scenario-4 

You can refer to

> https://www.mlflow.org/docs/latest/tracking.html

When you want to use server tracking you need to provide some variables

**Windows CMD**

````
SET MLFLOW_TRACKING_URI=xx.xx.xx.xx:5000
SET MLFLOW_S3_ENDPOINT_URL=xx.xx.xx.xx:9000
SET AWS_ACCESS_KEY_ID=<your username>
SET AWS_SECRET_ACCESS_KEY=<your password>
````


**Linux CMD**

````
export MLFLOW_TRACKING_URI=xx.xx.xx.xx:5000
export MLFLOW_S3_ENDPOINT_URL=xx.xx.xx.xx:9000
export AWS_ACCESS_KEY_ID=<your username>
export AWS_SECRET_ACCESS_KEY=<your password>
````

**Code in python**
````
import os
os.environ["MLFLOW_TRACKING_URI"] = "http://xx.xx.xx.xx:5000"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://xx.xx.xx.xx:9000"
os.environ["AWS_ACCESS_KEY_ID"] = "xxxxx"
os.environ["AWS_SECRET_ACCESS_KEY"] = "xxxx"
````

# Note
in docker-compose file we will see ${AWS_ACCESS_KEY_ID} ...
you should create a file with name: .env to run dokcer-compose

