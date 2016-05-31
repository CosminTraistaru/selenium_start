[![Build Status](https://travis-ci.org/CosminTraistaru/selenium_start.svg?branch=master)](https://travis-ci.org/CosminTraistaru/selenium_start)

This is a dummy repo for automated tests using python, selenium, pytest.
It is integrated with Travis CI.
It is failing to see a test failing and to see it's traceback.

In order to run localy you need to:
- clone the repo: 'git clone git@github.com:CosminTraistaru/selenium_start.git'
- create a virtualenv where you have to install the dependencies.
- 'virtualenv .env'
- 'source .env/bin/activate'
- 'pip install -r requirements.txt'
- and run the tests using py.test:
- 'py.test'
- A pretty results report is generated in the results.html file.
