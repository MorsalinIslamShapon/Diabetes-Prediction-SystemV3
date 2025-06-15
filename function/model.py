from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from function.transformers import ColumnSelector


selected_columns = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
]

# Pipeline setup
Model = Pipeline([
    ('column_selector', ColumnSelector(selected_columns)),
    ('model', RandomForestClassifier(max_depth=6,
                                     n_estimators=300,
                                     criterion='entropy'))
])