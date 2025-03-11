from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV
df = pd.read_csv('AP_Grama_Sachivalayam_Synthetic_Salaries.csv')

# Print column names to verify
print("CSV Columns:", df.columns.tolist())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    employee_id = request.form['employee_id']
    experience = float(request.form['experience'])

    # Use correct column name: 'EmployeeID'
    if employee_id in df['EmployeeID'].astype(str).values:
        base_salary = df[df['EmployeeID'].astype(str) == employee_id]['Monthly_Salary'].values[0]
        predicted_salary = base_salary + (experience * 1000)  # Simple logic
        return render_template('index.html', prediction=predicted_salary, employee_id=employee_id)
    else:
        return render_template('index.html', prediction="Employee ID not found", employee_id=employee_id)

if __name__ == '__main__':
    app.run(debug=True)
