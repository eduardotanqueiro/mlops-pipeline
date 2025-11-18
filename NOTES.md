 # Data
- Source:
https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data?resource=download


# Current Docker Commands
## DVC Pipeline
- Build Containerized Pipeline:
- docker build -f dvc-pipe.Dockerfile -t dvc-pipeline .
- Run Containerized Pipeline:
- docker run --rm -v ${PWD}:/app dvc-pipeline

## API
docker build -f api.Dockerfile -t penguin-api .
docker run -d -p 8000:8080 --name penguin_api penguin-api