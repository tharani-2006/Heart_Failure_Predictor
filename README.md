# Heart Failure Predictor ❤️

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Key Features](#key-features)
4. [Dataset Description](#dataset-description)
5. [Model Architecture](#model-architecture)
6. [Tech Stack](#tech-stack)
7. [Project Structure](#project-structure)
8. [Installation & Setup](#installation--setup)
9. [Running the Application](#running-the-application)
10. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
11. [Deployment](#deployment)
12. [Future Improvements](#future-improvements)
13. [Contributing](#contributing)
14. [License](#license)
15. [Contact](#contact)

---

## 🌟 Introduction

Heart failure is a critical medical condition where the heart is unable to pump blood effectively to meet the body's needs. It is a leading cause of mortality worldwide, affecting millions of individuals. Early detection and accurate prediction of heart failure risk are paramount for improving patient outcomes and reducing healthcare costs.

The **Heart Failure Predictor** is a machine learning-powered web application designed to assist healthcare professionals and individuals in assessing the risk of heart failure based on clinical parameters. By leveraging a dataset of clinical records, the application uses a trained Logistic Regression model to provide real-time predictions.

This project bridges the gap between complex machine learning algorithms and user-friendly interfaces, making predictive analytics accessible through a simple web-based dashboard built with Flask.

## ❗ Problem Statement

Despite advancements in medical technology, cardiovascular diseases (CVDs) remain the number one cause of death globally. According to the World Health Organization (WHO), an estimated 17.9 million people die from CVDs each year, representing 31% of all global deaths. Heart failure is a common consequence of CVDs.

Key challenges include:
- **Delayed Diagnosis**: Many patients are diagnosed only after significant heart damage has occurred.
- **Resource Constraints**: In many regions, access to expensive diagnostic tools like echocardiograms is limited.
- **Data Utilization**: Hospitals collect vast amounts of clinical data that often remain underutilized for proactive risk assessment.

Our goal is to create a tool that uses easily accessible clinical data (like age, serum creatinine levels, and ejection fraction) to predict the likelihood of heart failure with high accuracy.

## ✨ Key Features

- **Predictive Analytics**: Utilizes a Logistic Regression model for binary classification (Risk vs. No Risk).
- **Interactive UI**: A clean and responsive web interface for entering clinical data.
- **Real-time Processing**: Instant results upon form submission.
- **Data-Driven Insights**: Built on a foundation of exploratory data analysis performed on clinical records.
- **Scalable Backend**: Powered by Flask, allowing for easy integration of more complex models in the future.
- **Detailed Documentation**: Comprehensive guides for installation, usage, and development.

## 📊 Dataset Description

The model is trained on the **Heart Failure Clinical Records Dataset**, which contains 299 patients with heart failure. The dataset includes 13 clinical features that are known to be strong indicators of heart health.

### Feature Attributes Breakdown

| Feature | Description | Units | Type |
| :--- | :--- | :--- | :--- |
| **Age** | Age of the patient | Years | Numeric |
| **Anaemia** | Decrease of red blood cells or hemoglobin | Boolean | Binary (0/1) |
| **CPK** | Level of the CPK enzyme in the blood | mcg/L | Numeric |
| **Diabetes** | If the patient has diabetes | Boolean | Binary (0/1) |
| **Ejection Fraction** | Percentage of blood leaving the heart at each contraction | % | Numeric |
| **High Blood Pressure** | If the patient has hypertension | Boolean | Binary (0/1) |
| **Platelets** | Platelets in the blood | kiloplatelets/mL | Numeric |
| **Serum Creatinine** | Level of serum creatinine in the blood | mg/dL | Numeric |
| **Serum Sodium** | Level of serum sodium in the blood | mEq/L | Numeric |
| **Sex** | Woman (0) or man (1) | Binary | Binary (0/1) |
| **Smoking** | If the patient smokes | Boolean | Binary (0/1) |
| **Time** | Follow-up period | Days | Numeric |
| **Death Event** | If the patient died during the follow-up period | Target | Binary (0/1) |

### Selected Features for Prediction

For the initial version of the predictor, we selected high-impact features based on correlation analysis:
1. **Time**: The follow-up period significantly impacts the survival probability.
2. **Ejection Fraction**: A direct measure of heart functionality.
3. **Serum Creatinine**: An indicator of kidney function, which is closely linked to heart health.

## 🧠 Model Architecture

The core of this project is a Logistic Regression classifier. While simple, Logistic Regression provides high interpretability, which is crucial in medical applications where understanding the "why" behind a prediction is as important as the prediction itself.

### Training Pipeline

1. **Data Preprocessing**: Handling missing values (though this dataset is clean) and normalizing features.
2. **Feature Selection**: Using statistical methods to identify the most relevant columns.
3. **Train-Test Split**: Dividing the data (80% training, 20% testing) using `train_test_split` from Scikit-Learn.
4. **Model Training**: Fitting the `LogisticRegression` model to the training data.
5. **Serialization**: Saving the trained model instance to a `model.pkl` file using the `pickle` library.

### Performance Metrics

The model was evaluated using:
- **Accuracy Score**: The percentage of correct predictions.
- **Confusion Matrix**: To visualize true positives, true negatives, false positives, and false negatives.

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Web Framework**: Flask
- **Data Manipulation**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Environment Management**: venv
- **Model Storage**: Pickle

## 📁 Project Structure

```text
Heart_Failure_Predictor/
├── static/                  # CSS, JS, and Images
│   ├── style.css            # Custom styling for the dashboard
│   └── images/              # Project diagrams/screenshots
├── templates/               # HTML Templates
│   └── index.html           # Main application interface
├── app.py                   # Flask server and prediction logic
├── model.pkl                # Trained Logistic Regression model
├── heart_failure_prediction.ipynb # Jupyter Notebook for EDA/Training
├── heart_failure_clinical_records_dataset.csv # Raw dataset
├── requirements.txt         # Project dependencies
├── Procfile                 # Deployment configuration (e.g., Heroku)
├── .gitignore               # Files to ignore in Git
└── README.md                # Project documentation
```
