# py-csv-to-xlsx
Docker image to convert csv into complex xlsx.

### Start the build. 
#### Understand the environment variables 
1. ACCESS_KEY : Aws access key to run inside the AWS lambda env.
2. SECRET_KEY : Aws secret access key to run inside the AWS lambda env. 
3. BUCKET : Aws bucket name.
4. AWS_LAMBDA_RUNTIME_API: This will be ```mock``` to run in local.To Run inside AWS env use as per suggestion.
#### Build the image 
```
docker build --platform linux/amd64 -t <image-name> .
```

#### Run image locally 
```
docker run -d -p 9000:8080 --name python-lambda-s3 <image-name>:tag
```

### Test the lambda
```
curl --location 'http://localhost:9000/2015-03-31/functions/function/invocations' \
--header 'Content-Type: application/json' \
--data '{
    "filePath": "/home/input.csv",
    "template": "analytics"
}'
```