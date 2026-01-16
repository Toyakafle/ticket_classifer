import joblib

# Load the trained Logistic Regression model
loaded_classifier = joblib.load('logistic_regression_model.joblib')

# Load the TF-IDF Vectorizer
loaded_tfidf_vectorizer = joblib.load('tfidf_vectorizer.joblib')

def predict_category(input_text):
    # Preprocess the input text using the loaded TF-IDF vectorizer
    input_tfidf = loaded_tfidf_vectorizer.transform([input_text])

    # Make a prediction using the loaded classifier
    prediction = loaded_classifier.predict(input_tfidf)

    return prediction[0]
