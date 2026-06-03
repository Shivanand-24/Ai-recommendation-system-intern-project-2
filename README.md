# AI Data Classification Using Iris Dataset

## Project Overview

**AI Data Classification System** is a beginner-friendly Flask web application that demonstrates supervised machine learning using the Iris dataset. The application trains a Decision Tree classifier on app startup, accepts user input, and returns species predictions along with model confidence and accuracy.

This project is designed for a 2nd-year CSE student portfolio or review submission and focuses on clean code, modular structure, and professional presentation.

## Key Features

- Flask backend with routes for homepage, prediction form, and result page
- Uses `sklearn.datasets.load_iris()` directly — no external CSV required
- Decision Tree classification model trained automatically on startup
- Numeric input validation and error handling for user data
- Responsive UI with modern gradient and glassmorphism design
- Prediction breakdown with species label, confidence score, and model accuracy

## Tech Stack

- Python
- Flask
- Scikit-Learn
- Pandas
- NumPy
- HTML / CSS / JavaScript

## Installation

Open a terminal and install dependencies:

```bash
pip install -r requirements.txt
```

Alternatively, install each package manually:

```bash
pip install flask
pip install pandas
pip install numpy
pip install scikit-learn
```

## Run the Application

From the project root folder:

```bash
python app.py
```

Then open the app in your browser:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
AI-Classification/
├── app.py                  # Flask application routes and request handling
├── model.py                # Machine learning model training and prediction logic
├── requirements.txt        # Python dependencies for the project
├── README.md               # Project documentation
├── static/
│   ├── style.css           # Modern UI styling and responsive design
│   └── script.js           # Theme toggle and frontend validation
└── templates/
    ├── index.html          # Homepage dashboard
    ├── predict.html        # Prediction input form
    └── result.html         # Prediction result page
```


### Homepage
- Clean AI dashboard
- Model accuracy display
- Dataset summary

### Prediction Page
- Input fields for sepal and petal measurements
- Real-time validation

### Result Page
- Predicted Iris species
- Confidence score
- Model accuracy



## Future Enhancements

- Add additional classifiers such as Logistic Regression, KNN, and Random Forest
- Save and display previous predictions in browser storage or a database
- Add chart visualizations for prediction history and feature importance
- Enable custom dataset uploads and dynamic training

## Learning Outcomes

- Built a Flask project with a clear request-response flow
- Trained a supervised machine learning model using the Iris dataset
- Applied data preprocessing and evaluation best practices
- Implemented user input validation and error handling
- Designed a responsive user interface with an AI-inspired theme



This project emphasizes simplicity, readability, and professional structure. It demonstrates both backend Python skills and frontend presentation suitable for a college-level internship or coursework review.
