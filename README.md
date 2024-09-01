# Fake News Detection

## Overview

This project is designed to detect and classify fake news articles using machine learning techniques. The goal is to create a model that can automatically identify whether a given news article is real or fake based on its content.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [Results](#results)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8+
- pip
- Flask

## Usage

1. Clone this repository to your local machine:

bash
git clone https://github.com/2005Yaswi/fake-news-detection.git


2. Navigate to the project directory:

bash
cd fake-news-detection


3. Execute the Jupyter Notebook or Python scripts associated with each classifier to train and test the models. For example:

bash
python fakenews.py

## Dataset

- train.csv
- test.csv

## Model
We have used the four Mofels to get the best accuracy
1. *Logistic Regression*
2. *Decision Tree Classifier*
3. *Support Vector Machine*
4. *Random Forest Classifier*

The code will produce evaluation metrics and provide a prediction for whether the given news is true or false based on the trained model.

## Results
We evaluated each classifier's performance using metrics such as accuracy and achieved 90% above accuracy for each.


## Deployment
Developed a Flask web application integrated with machine learning models (Logistic Regression, Random Forest, Decision Trees) to automate fake news detection. Achieved high accuracy through comprehensive feature extraction and NLP-based preprocessing techniques.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.
For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.
You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.
## License

This project is licensed under the [MIT License](LICENSE).
