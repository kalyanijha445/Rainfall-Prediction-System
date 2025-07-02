from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model and accuracy
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

try:
    with open('accuracy.txt', 'r') as f:
        accuracy = float(f.read().strip())
except:
    accuracy = None  # fallback if file missing

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect')
def detect():
    return render_template('detect.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        timestamp = int(request.form['timestamp'])
        hash_val = request.form['hash']

        hash_length = len(str(hash_val))
        features = np.array([[timestamp, hash_length]])

        prediction = model.predict(features)[0]
        result = "Malware Detected 🔴" if prediction == 1 else "Safe ✅"

        return render_template("result.html", 
                               prediction=result, 
                               timestamp=timestamp, 
                               hash_value=hash_val, 
                               accuracy=accuracy)

    except Exception as e:
        return render_template("result.html", 
                               prediction=f"❌ Error: {str(e)}", 
                               timestamp="N/A", 
                               hash_value="N/A", 
                               accuracy=accuracy)

if __name__ == '__main__':
    app.run(debug=True)
