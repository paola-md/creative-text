# New Readme

# Local run

    sudo docker build -t creative-text .
    sudo docker run -p 80:80 --name creative-text --rm -ti creative-text

# Push to ECR

(First configure with `aws configure` to add account keys), then login with :

Without TTY terminal :

    sudo docker login -u AWS -p $(aws ecr get-login-password --region eu-central-1) 951661100876.dkr.ecr.eu-central-1.amazonaws.com

With TTY terminal :

    aws ecr get-login-password --region eu-central-1 | sudo docker login --username AWS --password-stdin 951661100876.dkr.ecr.eu-central-1.amazonaws.com

Then push with :

    sudo docker tag creative-text:latest 951661100876.dkr.ecr.eu-central-1.amazonaws.com/creative-text:latest

    sudo docker push 951661100876.dkr.ecr.eu-central-1.amazonaws.com/creative-text:latest

# (Old Readme)

* To run locally:
  * Go to folder:
    * Activate env: conda activate app-env
    * uvicorn creativity.app:app (in folder)
  * Test (http://127.0.0.1:8000/docs)

* Then add changes to github and they get automatically deployed. 


REPO_URL=paolamedo/creativity
BUILD_DIR=/Users/mejia/Documents/EPFL/projects/creative_text
docker build -t $REPO_URL .


docker build -t $REPO_URL $BUILD_DIR

docker run --rm -it  \
--net=host \
-v $BUILD_DIR:/home $REPO_URL


docker run --rm -it -e GRANT_SUDO=yes \
--user root \
-p 8888:8888 \
--net=host \
-e JUPYTER_TOKEN="easy" \
-v $BUILD_DIR:/home $REPO_URL 


docker run --rm -it $REPO_URL
 docker push $REPO_URL


 docker run -dp 3000:3000 my_docker_image
 


docker run --rm -it  \
-v $BUILD_DIR:/home $REPO_URL


docker tag $REPO_URL ic-registry.epfl.ch/d-vet/$REPO_URL

docker push ic-registry.epfl.ch/d-vet/$REPO_URL

1. `name_tag` is the name you gave to your image while building it




docker run --rm -it -e GRANT_SUDO=yes \
--user root \
-p 8888:8888 \
--net=host \
-e JUPYTER_TOKEN="easy" \
-v $HOME/.chef:/home/jovyan/.chef:ro \
-v $BUILD_DIR:/home/jovyan/work $REPO_URL
