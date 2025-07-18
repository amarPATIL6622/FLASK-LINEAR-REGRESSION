from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# ✅ Corrected file path
model = pickle.load(open(r'C:\Users\AMAR PATIL\Desktop\ai\linear regression\linear_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        x = float(request.form['x'])  # Change 'x' to actual input name if needed
        features = np.array([[x]])
        prediction = model.predict(features)
        return render_template('index.html', result=f'Predicted Value: {prediction[0]:.2f}')
    except Exception as e:
        return render_template('index.html', result=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
