 # Data
- Source:
https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data?resource=download


# Current Docker Commands
- Build Containerized Pipeline:
- docker build -f dvc-pipe.Dockerfile -t dvc-pipeline .
- Run Containerized Pipeline:
- docker run --rm -v ${PWD}:/app dvc-pipeline