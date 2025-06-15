import joblib
import pandas as pd
from sklearn.metrics import roc_auc_score
from function.model import Model

data = pd.read_csv('datasets/diabetes.csv')
X = data[['Pregnancies', 'Glucose','BloodPressure','SkinThickness', 'Insulin', 'BMI','DiabetesPedigreeFunction', 'Age']]
y = data['Outcome']

# Fit the model with grid search
Model.fit(X, y)

# Get the best model's predictions
y_pred = Model.predict_proba(X)[:, 1]

# Print the results
print("Best parameters:", Model.best_params_)
print("Best ROC-AUC Score: ", (roc_auc_score(y, y_pred) * 100).round(2))

# Save the best model
joblib.dump(Model.best_estimator_, 'model.pkl')