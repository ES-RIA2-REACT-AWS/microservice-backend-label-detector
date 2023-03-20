![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)


# Microservice Backend Label Validator

The goal of this project is to implement a microservice allowing the analysis of an image using the DetectLabels API (AWS). 

The principle is the following, a link must be submitted to our API, the image behind the link will then be analyzed by an AI which will then detect objects, concepts, and scenes in an image (JPEG or PNG).
The output will be the result of this analysis.

## Setting up dev

### Requirements

| Version            |  Description  | 
|--------------------|---|
| Python 3.10.7      | For code execution  |
| pip 23.0.1         | Python package manager  |
| virtualenv 20.16.3 | Python virtual environments tool|
 

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

- Set the project `app` directory to your `PYTHONPATH`.
- Copy `./example.secret.credentials.ini` and rename it to `./secret.credentials.ini`.
- Set the variable environment `CONFIG_FILE_PATH` to the path of your secret file `./secret.credentials.ini` 
- Set your credentials in `./secret.credentials.ini`

> Your secret file can be wherever you want, you just need to set the environment variable `CONFIG_FILE_PATH` properly.

#### Linux commands
1. Set the project `app` directory to your `PYTHONPATH`.
```sh
export PYTHONPATH="$PYTHONPATH:app"
```
2. Copy `./example.secret.credentials.ini` and rename it to `./secret.credentials.ini`.

```sh
cp ./example.secret.credentials.ini ./secret.credentials.ini
```
3. Set the variable environment `CONFIG_FILE_PATH` to the path of your secret file `./secret.credentials.ini` 
```sh
export CONFIG_FILE_PATH="./secret.credentials.ini"
```

4. Set your aws credentials.


### Run 

#### Local

Run FastAPI
```sh
uvicorn main:app --reload
```

### Configuration

The development environment requires to:
- Create the virtual environment
- Add the `src` directory to the PYTHONPATH
- Assign the environment variable
- Installing the library prerequisites in `requirements.txt`


##  Project directory structure

```sh
.
├── app
├── README.md
├── requirements.txt
├── tests
└── venv
```



| Directory | Description                                              | 
|-----------|----------------------------------------------------------|
| app/      | Project directory, contains the API, LabelDetector..     |
| tests/    | Test directory, contains Unittests and Integration tests |
| venv/     | Virtual environment                                      |
 



## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

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


## Licence

Distributed under the MIT License. See LICENSE for more information.