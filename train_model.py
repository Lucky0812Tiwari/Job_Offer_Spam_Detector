import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# 1. Load Data
df = pd.read_csv('fake_job_postings.csv')

# 2. Preprocess: Combine Title and Description for better context
df['full_text'] = df['title'].fillna('') + " " + df['description'].fillna('')
# Label is 'fraudulent' (0 for Real, 1 for Scam)

# 3. Split Data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(
    df['full_text'], df['fraudulent'], test_size=0.2, random_state=42
)

# 4. Create the ML Pipeline
# TF-IDF converts text to numbers based on importance
# Logistic Regression makes the final "Yes/No" decision
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('lr', LogisticRegression())
])

# 5. Train
print("Training the model... please wait.")
pipeline.fit(X_train, y_train)

# 6. Evaluate
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# 7. Save the "Brain" of your project
joblib.dump(pipeline, "scam_model_v1.pkl")
print("Model saved as scam_model_v1.pkl")