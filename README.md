# Diabetes Prediction with AI

![](https://github.com/Shankhadweep/Diabetes-Prediction-SystemV2/blob/main/Recording%202025-06-11%20102946.gif)


This project demonstrates a machine learning solution for predicting diabetes based on user-provided health data. The application uses **Streamlit** for an interactive web interface and advanced interpretability tools like SHAP and permutation importance to explain model predictions.

## Live Demo

Check out the live application: [Diabetes Prediction App](https://diabetes-prediction-systemv3-09.streamlit.app/)

---

## Table of Contents
1. [Overview](#overview)
2. [Dataset](#dataset)
3. [Model](#model)
4. [Features](#features)
5. [Installation](#installation)
6. [How It Works](#how-it-works)
7. [Project Structure](#project-structure)
8. [Explanation Methods](#explanation-methods)
9. [Model Performance](#model-performance)
10. [Project Motivation](#project-motivation)
11. [Contributing](#contributing)
12. [License](#license)


---

## Overview

The **Diabetes Prediction with AI** project leverages a machine learning model to predict diabetes risk. Built with **Streamlit**, the app explains predictions using SHAP and permutation importance while showcasing model performance metrics. This model has not been reviewed by medical professionals; it is developed solely for experimental and testing purposes.
The model was developed based on the ROC AUC metric, while efforts were made to improve the Recall metric when selecting the threshold, as this decision was made due to the medical context.

### Why This Project?

Understanding diabetes risk through data-driven predictions can help identify potential cases early. This project also demonstrates:
- Practical application of machine learning.
- Model interpretability through SHAP and permutation importance.
- Real-world deployment of machine learning models.

---

## Dataset

The dataset is sourced from the **National Institute of Diabetes and Digestive and Kidney Diseases**. It includes:

The dataset contains the following details:

### General Overview
- **Number of rows:** 3001
- **Number of columns:** 9
- **Column names and data types:**
  - `Pregnancies` (int64): Number of times pregnant.
  - `Glucose` (int64):  Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
  - `BloodPressure` (int64): Diastolic blood pressure (mm Hg).
  - `SkinThickness` (int64): Triceps skin fold thickness (mm).
  - `Insulin` (int64): 2-Hour serum insulin (mu U/ml).
  - `BMI` (float64): Body mass index (weight in kg/(height in m)^2).
  - `DiabetesPedigreeFunction` (float64): Diabetes pedigree function.
  - `Age` (int64): Age (years).
  - `Outcome` (int64): Class variable (0 or 1).

### Sample Data (First 5 Rows)
| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin |  BMI  | DiabetesPedigreeFunction | Age | Outcome |
|-------------|---------|---------------|---------------|---------|-------|---------------------------|-----|---------|
| 6           | 148     | 72            | 35            | 0       | 33.6  | 0.627                     | 50  | 1       |
| 1           | 85      | 66            | 29            | 0       | 26.6  | 0.351                     | 31  | 0       |
| 8           | 183     | 64            | 0             | 0       | 23.3  | 0.672                     | 32  | 1       |
| 1           | 89      | 66            | 23            | 94      | 28.1  | 0.167                     | 21  | 0       |
| 0           | 137     | 40            | 35            | 168     | 43.1  | 2.288                     | 33  | 1       |

### Statistical Summary
- **Pregnancies:** Mean = 3.85, Max = 17
- **Glucose:** Mean = 120.89, Min = 0 (possible missing values)
- **BloodPressure:** Mean = 69.11, Min = 0 (possible missing values)
- **SkinThickness:** Mean = 20.54, Min = 0 (possible missing values)
- **Insulin:** Mean = 79.80, Min = 0 (possible missing values)
- **BMI:** Mean = 31.99, Min = 0 (possible missing values)
- **DiabetesPedigreeFunction:** Mean = 0.47, Max = 2.42
- **Age:** Mean = 33.24, Max = 81
- **Outcome:** Proportion of `1` (positive diabetes) = 34.9%


#### We use only `Pregnancies`, `Glucose`, `BMI`, `Insulin`, `Age` for prediction.
---

## Model
You can learn more about the model in detail from [here](notebooks/Model.ipynb). The `RandomForestClassifier` model was chosen through experimentation and showed the best performance. pipeline.
 `ROC AUC` were used for model selection because the number of observations was small, and splitting into test/train sets would have been inaccurate.

### About tarnsformers

#### **3. ColumnSelector**
Selects specific columns *Pregnancies*, *Glucose*, *BMI*, *PregnancyRatio*,
    *RiskScore*, *InsulinEfficiency*, *Glucose_BMI*, *BMI_Age*,
    *Glucose_woe*, *RiskScore_woe* after `FeatureEngineering`, it helps remove noice columns.

---
## Features

1. **Interactive Input**: Enter health parameters (Pregnancies,Glucose,Blood Pressure,Skin Thickness,Insulin,BMI,Diabetes Pedigree Function,Age).
2. **Diabetes Prediction**: Real-time risk prediction with probability.
3. **SHAP Explanations**: Visualize individual prediction explanations using:
   - Waterfall Plot
   - Force Plot
4. **Permutation Importance**: Analyze which features most influence the predictions.
5. **Performance Metrics**:
   - Accuracy
   - Precision
   - Recall
   - F1 Score
   - ROC AUC
6. **Informational Section**: Learn about diabetes risk factors in the "About" section.

---

## Installation

### Prerequisites
- Python 3.10 or above
- Pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Shankhadweep/Diabetes-Prediction-SystemV3.git
   cd Diabetes-Prediction
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   streamlit run main.py
   ```

---

## How It Works

### Application Workflow
1. **User Input**:
   - Enter health data in the sidebar.
   - Features: Pregnancies,Glucose,Blood Pressure,Skin Thickness,Insulin,BMI,Diabetes Pedigree Function,Age.
2. **Prediction**:
   - The trained model predicts diabetes risk and displays the result.
3. **Explanation**:
   - View SHAP plots (Waterfall and Force) for detailed feature contributions.
   - Explore permutation importance for global feature analysis.
4. **Model Performance**:
   - Metrics such as Accuracy, F1 Score, and ROC AUC are displayed.


# Project Structure
```
Diabetes-Prediction/
├── README.md                 # Project documentation
├── main.py                   # Entry point for the Streamlit app
├── loader.py                 # Data loading and preprocessing
├── training.py               # Script for training the model
├── requirements.txt          # Project dependencies
├── LICENSE                   # License file
├── datasets/
│   ├── diabetes.csv          # Dataset used for training and predictions
├── models/
│   ├── model.pkl             # Trained machine learning model
├── images/
│   ├── page_icon.jpeg        # Application page icon
├── data/
│   ├── config.py             # Configuration variables
│   ├── base.py               # Static HTML/CSS content
├── functions/
│   ├── model.py              # Custom model implementation
│   ├── function.py           # Utility functions
└── app/                      # Application logic and components
    ├── predict.py            # Prediction logic
    ├── explainer.py          # SHAP-based explanations
    ├── perm_importance.py    # Permutation importance analysis
    ├── performance.py        # Visualization of model performance metrics
    ├── input.py              # User input handling for predictions
    ├── about.py              # Informational section on diabetes
```


---

## Explanation Methods

1. **SHAP Waterfall Plot**:
   - Shows how each feature contributes positively or negatively to the prediction.
2. **SHAP Force Plot**:
   - Interactive visualization of feature contributions to individual predictions.
3. **Permutation Importance**:
   - Ranks features by their impact on the model's predictions.

---

## Model Performance

Performance metrics calculated:
- **Accuracy**: Percentage of correct predictions. (0.998)
- **Precision**: Ratio of true positives to total positive predictions. (0.9943)
- **Recall**: Ratio of true positives to total actual positives. (1.0000)
- **F1 Score**: Harmonic mean of Precision and Recall. (0.9971)
- **ROC AUC**: Area under the ROC curve. (1.0000)

Metrics are displayed as donut charts in the application.

---

## Project Motivation

This project was developed to:
- Build knowledge in machine learning, especially in healthcare.
- Gain hands-on experience with model interpretability techniques like SHAP.
- Deploy an AI solution using **Streamlit**.

---

## Contributing

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Feature description"
   git push origin feature-name
   ```
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



### <i>Thank you for your interest in the project!</i>
