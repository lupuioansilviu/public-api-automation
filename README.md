# API Automation Framework (Pytest + Requests)

## Overview

This project contains an automated API test framework written in Python using:

- *Pytest* as the test runner
- *Requests* for HTTP communication
- Parametrized tests for scalable coverage

This API is listed in the `public-apis/public-apis` repository.
Base URL: https://api.agify.io  
API: **Agify.io**

---

## Framework POM

The project follows the following structure:

public-api-automation/
    - src
    - init.py
    - api_client

    - tests
    - init.py
    - test_public_api.py

    - pytest.ini
    - requirements.txt
    - READE.md 


## Installation

````
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

running tests - pytest -q

Python 3.9+ (required)
Pytest
Requests
````

## Test cases:

## Test Cases

| ID     | Test Name                                        | Endpoint                              | Validation |
|--------|--------------------------------------------------|---------------------------------------|------------|
| API-01 | Predict age returns 200 (parametrized)           | `GET /?name={name}`                   | Status code = 200 |
| API-02 | Predict age response schema (parametrized)       | `GET /?name={name}`                   | Keys exist (`name`, `age`, `count`); `count` is int; `age` is int or null |
| API-03 | Predict age with country_id schema (parametrized)| `GET /?name={name}&country_id={country}` | Status 200; keys exist; `name` matches request |
| API-04 | Predict age with empty name returns expected keys| `GET /?name=`                         | Status 200; keys exist; no error response |

## Demo Gif

![Test execution](docs/run.gif)