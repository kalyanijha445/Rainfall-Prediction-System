import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

def train_model():
    try:
        # Load dataset
        df = pd.read_csv('malware_deep.csv')

        # Feature engineering
        df['hash_length'] = df['hash'].astype(str).apply(len)
        X = df[['timestamp', 'hash_length']]
        y = df['malware']

        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Save model
        with open('model.pkl', 'wb') as f:
            pickle.dump(model, f)

        # Evaluate model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Save accuracy for result.html
        with open('accuracy.txt', 'w') as f:
            f.write(f"{accuracy*100:.2f}")

        print(f"✅ Model trained and saved. Accuracy: {accuracy*100:.2f}%")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    train_model()
