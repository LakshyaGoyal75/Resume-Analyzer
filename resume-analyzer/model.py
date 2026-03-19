import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("resume_dataset.csv")

X = data["skills"]
y = data["role"]

vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vector, y)

def predict_role(skills):
    skills_vector = vectorizer.transform([skills])
    prediction = model.predict(skills_vector)
    return prediction[0]