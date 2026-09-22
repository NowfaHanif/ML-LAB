import joblib
import numpy as np
import pandas as pd

model = joblib.load("digital_wellbeing_random_forest.joblib")

def predict_digital_wellbeing(values):
    user = pd.DataFrame([values])
    score = float(np.clip(model.predict(user)[0], 0, 100))

    if score >= 70:
        level = "Good"
    elif score >= 50:
        level = "Moderate"
    else:
        level = "Needs Attention"

    return round(score, 2), level


if __name__ == "__main__":
    sample_user = {
        "daily_screen_time_min": 360,
        "num_app_switches": 48,
        "sleep_hours": 7.5,
        "notification_count": 75,
        "social_media_time_min": 100,
        "focus_score": 7.5,
        "mood_score": 8.0,
        "anxiety_level": 4.0
    }

    score, level = predict_digital_wellbeing(sample_user)

    print("Predicted Digital Wellbeing Score:", score)
    print("Wellbeing Level:", level)
