# Usage

## Build the image 

`docker build -t <> .`

## Run the container
`docker run -p 8080:8080 <image_name:version>`

## Api

Api endpoint 
`/users/{user_id}`

Authentication to github is not required as it's getting the public gist of the user