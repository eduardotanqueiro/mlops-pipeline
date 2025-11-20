# MLOps - Pipeline
This repository contains a simple MLOps pipeline, with a focus on automation, versioning, and reproducibility.
This mini-project was developed to deepen my knowledge in DevOps practices applied to Machine Learning, including data versioning, CI/CD, containerization, branch management, and automated testing. It was not created for production use.

A light dataset is used to keep the project simple and focused on MLOps practices rather than model performance. The model used was a Random Forest Classifier trained on the [Palmer Archipelago (Antarctica) penguin data](https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data?resource=download). The goal is to classify penguin species based on physical measurements.

## 1. Overview
This project contains a pipeline that includes data preprocessing, model training, evaluation, model serving through an API, and deployment using Docker and CI/CD tools.

- Reproducible training workflow (using DVC)
- Containerized training & evaluation
- REST API for model serving (FastAPI)
- Data & model versioning (DVC)
- Automated tests (integration)
- CI with GitHub Actions
- CD with Render (auto-deployment on push to main and CI pass, Docker-based)

## 2. Tech Stack
- Python
- FastAPI
- Docker
- GitHub Actions
- DVC (Data Version Control)
- Render (for deployment)

## 3. Project Structure
```
mlops-pipeline/
│
├── api/                    # FastAPI inference service
│   ├── main.py             # API entrypoint
│   ├── core/               # .env loading & settings
│   ├── models/             # Model Loader Logic
│   ├── routes/             # API Endpoints
│   ├── schemas/            # Pydantic Schemas for input/output validation 
│   ├── services/           # Utility services (e.g., prediction logic)
│
├── ckpt/                   # Trained model (versioned, DVC/Git-ignored)
│
├── data/                   # Raw & processed data (DVC/Git-ignored, source above)
│
├── model/                  # Data preprocessing, training & evaluation scripts
│
├── tests/                  # PyTest-based integration tests
│
├── api.Dockerfile          # Dockerfile for inference API
├── docker-compose.yml      # Simple local API environment
├── dvc-pipe.Dockerfile     # Dockerfile for training & evaluation pipeline (using DVC)
├── dvc.yaml                # DVC pipeline definition
│
├── params.yaml             # Data Paths
├── requirements.txt        # Python dependencies (Train & Eval)
├── requirements_api.txt    # Python dependencies (API)
│
├── .github/
│   └── workflows/
│       ├── ci.yml          # Linting, PyTest, Docker Image Build Test
│
└── README.md               # This file
```

## 4. Features
### Reproducible ML Pipeline
- Entire workflow defined through scripts (dvc.yaml pipeline, only one command training (dvc repro) and run on a container environment)
- Deterministic model training
- Dataset & model tracked (local or via DVC)

### API for Inference
- FastAPI server exposing prediction endpoint
- Dockerized for stable deployment

### CI (GitHub Actions)

- Linting & integration tests with PyTest, validating endpoints on edge cases
- Training on a light dataset subset    
Evaluation & metric validation


## 5. Setup Instructions

1) Prerequisites
- Install [Docker](https://docs.docker.com/get-docker/)
- Install Git

2) Clone the Repository
    ```bash 
    git clone https://github.com/eduardotanqueiro/mlops-pipeline.git
    
    cd mlops-pipeline
    ```
3) Download the dataset and place the  ```penguins_size.csv``` in the `data/raw/` directory.
    - In a real production environment, this would be done with ```dvc pull``` from a remote storage. However, for educational purposes, only local storage was used in this project

4) Build and Run DVC Training and Evaluation Pipeline in a Containerized Environment
    ```bash
    docker build -f dvc-pipe.Dockerfile -t dvc-pipeline .

    docker run --rm -v ${PWD}:/app dvc-pipeline

    cp ckpt/model.pkl api/models/model.pkl
    ```
5) Build and Run the API localy in a Containerized Environment
    ```bash
    docker compose up
    ```

## 6. Testing the API
You can test the API using curl or any API testing tool like Postman. Here are some example curl commands:
- Get API Root check:
    ```bash
    curl -X GET "http://localhost:8000/"
    ```
- Predict penguin species:
    - Valid input example:
        ```bash
        curl -X POST "http://localhost:8000/predict" -H "Content-Type:application/json" -d '{"features": [1, 46.9, 14.6, 222.0, 4875.0, 1]}'
        ```
    - Invalid input example (to test error handling):
        ```bash
        curl -X POST "http://localhost:8000/predict" -H "Content-Type:application/json" -d '{"features": [1, "string!", 14.6, 222.0, 4875.0, 1]}'
        ```

Note: these feature values correspond to:
- Islan
- Culmen Length (mm)
- Culmen Depth (mm)
- Flipper Length (mm)
- Body Mass (g)


## 7. References/Sources
This project was inspired by various MLOps resources and tutorials available online, including:
- [GitHub Actions For Machine Learning Beginners](https://www.kdnuggets.com/github-actions-for-machine-learning-beginners)
- [CI/CD for ML with GitHub Actions – Automate Test-Train-Deploy Pipelines](https://aviraj.info/mlops/cicd-github-actions.html)
- [DVC Documentation](https://dvc.org/doc/start)

It was also developed leveraging AI agents (ChatGPT and GitHub Copilot) to efficiently help in the learning process, aiding in code generation, project structuring, and debugging.
