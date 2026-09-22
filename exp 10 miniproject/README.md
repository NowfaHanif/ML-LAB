# Digital Wellbeing Score Prediction Using Random Forest

A Machine Learning mini project that predicts a **Digital Wellbeing Score (0–100)** using a **Random Forest Regressor**.

## Problem Statement

Digital habits such as screen time, social-media usage, app switching and notifications can be considered together with sleep, focus, mood and anxiety to estimate an overall digital wellbeing score.

## Algorithm Used

**Random Forest Regressor**

Random Forest builds multiple decision trees and averages their predictions. It works well for nonlinear regression problems and provides feature-importance values.

## Dataset

The included file `digital_wellbeing_dataset.csv` contains **500 rows and 9 columns**.

### Input Features

- `daily_screen_time_min`
- `num_app_switches`
- `sleep_hours`
- `notification_count`
- `social_media_time_min`
- `focus_score`
- `mood_score`
- `anxiety_level`

### Target

- `digital_wellbeing_score`

### Dataset Source Note

The project follows the feature structure of the public Kaggle dataset:

**Mental Health and Digital Behavior (2020–2024)**  
https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-digital-behavior-20202024

The public dataset is described as simulated. To keep this repository completely reproducible without Kaggle login/API credentials, the included CSV is a deterministic educational dataset generated with the same core feature structure and similar ranges.

## Model Performance

Using an 80/20 split:

- **MAE:** 2.45
- **RMSE:** 3.13
- **R² Score:** 0.9286
- **Variance explained:** 92.86%

## Project Workflow

```text
Dataset
   ↓
Data Exploration
   ↓
Correlation Analysis
   ↓
Train-Test Split
   ↓
Random Forest Regressor
   ↓
Prediction
   ↓
MAE / RMSE / R²
   ↓
Actual vs Predicted Plot
   ↓
Feature Importance
   ↓
Custom User Prediction
```

## Repository Files

```text
Digital_Wellbeing_Score_Prediction_Random_Forest.ipynb
digital_wellbeing_dataset.csv
digital_wellbeing_random_forest.joblib
predict_wellbeing.py
requirements.txt
.gitignore
README.md
```

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Then open:

```text
Digital_Wellbeing_Score_Prediction_Random_Forest.ipynb
```

Run all cells in Google Colab or Jupyter Notebook.

## Custom Prediction

The notebook includes a function where a user can enter:

- Screen time
- App switches
- Sleep hours
- Notification count
- Social media time
- Focus score
- Mood score
- Anxiety level

The model returns a predicted **Digital Wellbeing Score** and a simple level:

- Good
- Moderate
- Needs Attention

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Google Colab / Jupyter Notebook

## Disclaimer

This project is for **educational purposes only** and is not a medical or psychological diagnostic tool.
