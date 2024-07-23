# py-csv-to-xlsx
Docker image to convert csv into complex xlsx.

### Start the build. 
#### Understand the environment variables 
1. input : The input .csv file path
2. AWS_ACCESS_KEY_ID : Aws access key to run inside the AWS lambda env.
3. AWS_SECRET_ACCESS_KEY : Aws secret access key to run inside the AWS lambda env. 
4. AWS_LAMBDA_RUNTIME_API: This will be ```mock``` to run in local.To Run inside AWS env use as per suggestion.

#### Build the image 
```
docker build --platform linux/amd64 -t <image-name> .
```

#### Run image locally 
```
docker run -d -p 9000:8080 --name python-s3 --env=input="/home/input.csv" <image-name>:tag
```