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

## Installation

### Prerequisites

- Python 3.8+
- pip
- Flask

## Usage

1. Clone this repository to your local machine:

bash
git clone https://github.com/kolliparatanusree/Fake_News_Detection.git


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
