from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from function.transformers import ColumnSelector


selected_columns = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
]

# Define the pipeline
base_pipeline = Pipeline([
    ('column_selector', ColumnSelector(selected_columns)),
    ('model', RandomForestClassifier(random_state=42))
])

# Define hyperparameter grid
param_grid = {
    'model__n_estimators': [200, 300, 400, 500],
    'model__max_depth': [6, 8, 10, 12],
    'model__min_samples_split': [2, 5, 10],
    'model__min_samples_leaf': [1, 2, 4],
    'model__criterion': ['gini', 'entropy'],
    'model__max_features': ['sqrt', 'log2']
}

# Create GridSearchCV object
Model = GridSearchCV(
    estimator=base_pipeline,
    param_grid=param_grid,
    cv=5,
    scoring='roc_auc',
    n_jobs=-1,
    verbose=1
)