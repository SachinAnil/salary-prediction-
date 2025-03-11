from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Load dataset
df = pd.read_csv("AP_Grama_Sachivalayam_Synthetic_Salaries.csv")

# Check column names
print("Columns in CSV:", df.columns)

# Prepare training data
X = df[['Years_of_Experience']]
y = df['Monthly_Salary']

# Train the model
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        experience = float(request.form['experience'])
        prediction = model.predict(np.array([[experience]]))[0]
        prediction = round(prediction, 2)
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)




