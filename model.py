import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


class DataModel:
    def __init__(self):
        self.dataset = load_iris()
        self.data = pd.DataFrame(self.dataset.data, columns=self.dataset.feature_names)
        self.data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        self.data['species'] = pd.Categorical.from_codes(self.dataset.target, self.dataset.target_names)
        self.scaler = StandardScaler()
        self.classifier = DecisionTreeClassifier(random_state=42)
        self.train_model()

    def train_model(self):
        X = self.data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
        y = self.data['species']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        self.classifier.fit(self.X_train_scaled, self.y_train)
        self.accuracy = float(self.classifier.score(self.X_test_scaled, self.y_test))

    @property
    def summary(self):
        return {
            'accuracy': self.accuracy,
            'rows': self.data.shape[0],
            'cols': self.data.shape[1],
            'preview': self.data.head(8).to_dict(orient='records'),
        }

    def predict(self, feature_values):
        features = np.array(feature_values).reshape(1, -1)
        features_scaled = self.scaler.transform(features)
        predicted = self.classifier.predict(features_scaled)[0]
        confidence = float(np.max(self.classifier.predict_proba(features_scaled)[0]))
        return predicted, confidence, self.accuracy
