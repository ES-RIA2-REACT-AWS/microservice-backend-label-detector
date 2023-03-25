![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![]()

# Microservice Backend Label Validator

The goal of this project is to implement a microservice allowing the analysis of an image using the DetectLabels API (
AWS).

The principle is the following, a link must be submitted to our API, the image behind the link will then be analyzed by
an AI which will then detect objects, concepts, and scenes in an image (JPEG or PNG).
The output will be the result of this analysis.

## Table of content

1. [Setting up dev](#setting-up-dev)
2. [Run](#run)
3. [Testing](#testing)
4. [Docker](#docker)
5. [Project directory structure](#project-directory-structure)
6. [Contributing](#contributing)
7. [License](#license)

## Setting up dev

### Requirements

| Version            | Description                      | 
|--------------------|----------------------------------|
| Python 3.10.7      | For code execution               |
| pip 23.0.1         | Python package manager           |
| virtualenv 20.16.3 | Python virtual environments tool |

### Clone repository

```sh
git clone git@github.com:ES-RIA2-REACT-AWS/microservice-backend-label-detector.git
cd microservice-backend-label-detector/
git switch develop
```

### Install dependencies

```sh
pip3 install -r requirements.txt 
```

### Local configuration

- Add to your `PYTHONPATH` the complete path to the project `app` directory.
- Copy `./example.secret.credentials.ini` and name it `./secret.credentials.ini`.
- Set the variable environment `CONFIG_FILE_PATH` to the path of your secret file `./secret.credentials.ini`
- Set your credentials in `./secret.credentials.ini`

> Your secret file can be wherever you want, you just need to set the environment variable `CONFIG_FILE_PATH` properly.

#### Linux environment

```sh
# Set the project `app` directory to your `PYTHONPATH`.
export PYTHONPATH="$PYTHONPATH:app"
# Copy `./example.secret.credentials.ini` and rename it to `./secret.credentials.ini`
cp ./example.secret.credentials.ini ./secret.credentials.ini
# Set the variable environment `CONFIG_FILE_PATH` to the path of your secret file `./secret.credentials.ini`
export CONFIG_FILE_PATH="./secret.credentials.ini"
````

Then set your aws credentials.

## Run

Here is the `FastAPI` command to run the project

```sh
uvicorn app.main:app --reload --port 5000
```

## Testing

The tests can be run by the following `unittest` commands

```sh
# Search all tests
python -m unittest discover -v
# Integration test only
python -m unittest tests.integration.test_label_detector_analyze -v
```

## Docker

### Docker requirements

| Version                                                             | Description                          | 
|---------------------------------------------------------------------|--------------------------------------|
| [Docker 23.0.0](https://docs.docker.com/engine/install/ubuntu/)     | Set of PaaS                          |
| [Docker Compose V2](https://docs.docker.com/compose/install/linux/) | tool for deploying Docker containers |

### Docker compose

The current project has 3 different containers implemented in the Dockerfile: `production`, `development` and `tests`.

Procedure to run `development`:

```sh
docker compose build development
docker compose up development -d
```

You should be able to access to the `Swagger tool` from `http://0.0.0.0:5000/docs#`.

You can also run tests through this command:

```sh
docker compose exec development python -m unittest tests.integration.test_label_detector_analyze -v
```

Stop `development`

```sh
docker compose stop development
```

## Project directory structure

```sh
.
├── app
│   ├── config
│   ├── controllers
│   ├── handlers
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   └── services
├── config.env
├── docker-compose.yaml
├── Dockerfile
├── example.secret.credentials.ini
├── README.md
├── requirements.txt
├── secret.credentials.ini
└── tests
    ├── __init__.py
    ├── integration
    └── unit

```

## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/amazing_feature)
3. Commit your Changes (git commit -m 'Add some amazing_feature')
4. Push to the Branch (git push origin feature/amazing_feature)
5. Open a Pull Request

> If the changes in your branch involve the use of external python packages, please update the requirements:
> `pip3 freeze > requirements.txt`
>
> If these packages are specific to the development environment, please create a new one:
> `pip3 freeze > requirements_dev.txt`

## License

Distributed under the MIT License. See LICENSE for more information.