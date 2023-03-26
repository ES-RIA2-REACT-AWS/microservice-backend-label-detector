![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


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

### Local configuration
1. Add to your `PYTHONPATH` the complete path to the project `app` directory.
    
    **For Windows**:
    Refer to this [post](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages). Make sure to set the full path to the `app` folder

    **For Linux**
    ```shell
    export PYTHONPATH="$PYTHONPATH:app"
    ```
2. Copy `./example.env` and name it `./.env`.
3. Set your credentials and the project name in new `.env`
4. If your IDE does not create the virtual environment you need to create it yourself:
    ```sh
    python3 -m venv .venv
    ```
   To activate it, run this command: `source .venv/bin/activate`
   To deactivate it, run this command: `source .venv/bin/deactivate` 
   For Windows, refer to the official [documentation](https://docs.python.org/3/tutorial/venv.html).

### Install dependencies

```sh
pip3 install -r requirements.txt 
```

## Run

Here is the `FastAPI` command to run the project

```sh
uvicorn app.main:app --reload --port 5000
```

## Testing

The tests can be run by the following `unittest` commands

Run all tests:
```sh
python3 -m unittest discover -v
```

Run the integration test:
```sh
python3 -m unittest tests.integration.test_label_detector_analyze -v
```

## Docker

The current project has 3 different images implemented in the `Dockerfile`.
- `ria2_label_detector_aws:production` : Run FastAPI.
- `ria2_label_detector_aws:development` : Contains the test directory, start by running FastAPI
- `ria2_label_detector_aws:tests` : Run unit and integration tests

### Docker requirements

| Version                                                             | Description                          | 
|---------------------------------------------------------------------|--------------------------------------|
| [Docker 23.0.0](https://docs.docker.com/engine/install/ubuntu/)     | Set of PaaS                          |
| [Docker Compose V2](https://docs.docker.com/compose/install/linux/) | tool for deploying Docker containers |

### Docker compose

The current project has 3 different services implemented in the `docker-compose.yml`: `production`, `development` and `tests`.

Procedure to run `development`:
1. Build
    ```sh
    docker compose build development
    ```
2. Run
    ```sh
    docker compose up development -d
    ```
    You should be able to access to the `Swagger tool` from `http://0.0.0.0:5000/docs#`.

3. You can also run tests through this command: `compose exec development`
    ```sh
    docker compose exec development python -m unittest tests.integration.test_label_detector_analyze -v
    ```

4. Stop `development`
    ```sh
    docker compose stop development
    ```

## Project directory structure

```sh
.
├── app
│   ├── controllers
│   ├── handlers
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   └── services
├── docker-compose.yml
├── Dockerfile
├── example.env
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── integration
    └── unit
```

- `controllers`: contains the controller in which the POST method is submitted
- `handlers`   : contains the handlers that translate service exceptions into server errors
- `models`     : contains the expected input data models
- `services`   : contains the API services
- `tests`      : contains the unit and integration tests
- `main.py`    : application entry point
- `example.env`: project config file that contains the required env variables (credentials etc..)

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