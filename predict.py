import pickle
import pandas as pd

def predict_malware(timestamp, hash_value):
    try:
        # Load model
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Prepare features
        hash_length = len(str(hash_value))
        X = pd.DataFrame([[timestamp, hash_length]], columns=['timestamp', 'hash_length'])

        # Predict
        prediction = model.predict(X)[0]

        # Load accuracy from file
        with open('accuracy.txt', 'r') as f:
            acc = f.read()

        return prediction, acc

    except Exception as e:
        return f"Error: {e}", None
