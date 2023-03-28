![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


# Microservice Backend Label Validator

The goal of this project is to implement a microservice allowing the analysis of an image using the DetectLabels API (
 AWS rekognition).

The principle is the following, a link must be submitted to our API, the image behind the link will be analyzed by
an AI which will detect objects, concepts, and scenes.


## Table of content

1. [Setting up dev](#setting-up-dev)
   1. [Requirements](#requirements)
   2. [Clone repository](#clone-repository)
   3. [Configuration](#configuration)
   4. [Dependencies installation](#dependencies-installation)
   5. [Run](#run)
   6. [Testing](#testing)
2. [Docker](#docker)
   1. [Docker requirements](#docker-requirements)
   2. [Docker compose](#docker-compose)
3. [Project directory structure](#project-directory-structure)
4. [Contributing](#contributing)
5. [Credits](#credits)
6. [License](#license)
7. [Best practices](#best-practices)

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

### Configuration
To install and run this project locally, follow these steps:

1. Clone this repository onto your local machine.
2. Open a terminal window and navigate to the root directory of the project.
3. Add to your `PYTHONPATH` the complete path to the project `app` directory.
    
    **For Windows**:
    Refer to this [post](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages). Make sure to set the full path to the `app` folder

    **For Linux**
    ```shell
    export PYTHONPATH="$PYTHONPATH:app"
    ```
4. Copy `./.env.example` and name it `./.env`.
5. Set your credentials and the project name in new `.env`
6. If your IDE does not create the virtual environment you need to create it yourself:
    ```sh
    python3 -m venv .venv
    ```
   To activate it, run this command: `source .venv/bin/activate`
   To deactivate it, run this command: `source .venv/bin/deactivate` 
   For Windows, refer to the official [documentation](https://docs.python.org/3/tutorial/venv.html).

###  Dependencies installation

```sh
pip3 install -r requirements.txt 
```

### Run

Here is the `FastAPI` command to run the project

```sh
uvicorn app.main:app --reload --port 5000
```

FastAPI has the [Swagger UI](https://fastapi.tiangolo.com/features/#automatic-docs) tool integrated. 
Follow these step if you want to use it:
1. Run the project with `uvicorn app.main:app --reload --port 5000` command.
2. Open your Browser and navigate to [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/)
3. Clic on `Try it out`
4. You can copy past your `image_url`, `max_label` and `min_confidence_level`

### Testing
The test framework for this project is [unittest](https://docs.python.org/3/library/unittest.html)

The tests can be run by the following commands:

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
    docker compose exec development python3 -m unittest discover -v
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
├── .env.example
├── LICENSE
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
- `.env.example`: project config file that contains the required env variables (credentials etc..)

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

## Credits
This project uses the following technologies:

- FastApi
- Pydantic validators
- Python Unittest

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the LICENSE file for more details

## Best practices

Practices and documentation on which this project is based:

- [Python Style Guide (PEP 8)](https://peps.python.org/pep-0008/)
- [Python naming convention (PEP8)](https://peps.python.org/pep-0008/#naming-conventions)
- [Docker best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Unittest documentation](https://docs.python.org/3/library/unittest.html)
- [Pydantic validators](https://docs.pydantic.dev/usage/validators/)

### Notes
The snake case naming convention is not respected in the `unit and integration tests` for the methods: `setUpClass`, `tearDownClass`, `tearDown` and `setUp`. These are the methods of the test framework. 
Unittest being based on Jest, it does not respect the python naming convention.
